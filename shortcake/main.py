from typing import Optional, List
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
import uvicorn

import models, schemas
from schemas import Link
from db import SessionLocal, Base, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


def get_db():
    """Database dependency
    This dependency creates a new SessionLocal used for a single
    request and closes when request is completed.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/", status_code=status.HTTP_200_OK)
def main(db: Session = Depends(get_db)):
    """Show all links upon entry
    """
    return db.query(models.Link).all()


@app.get("/links", response_model=List[schemas.Link])
def show_links(db: Session = Depends(get_db)):
    links = db.query(models.Link).all()
    return links


@app.post("/add-link", response_model=schemas.Link)
def create_link(link: Link, db: Session = Depends(get_db)):
    """Create a new link and add to db
    """
    # Check if target link already exists
    db_link = db.query(models.Link).filter(models.Link.long_link==link.long_link).first()

    if db_link is not None:
        raise HTTPException(status_code=400, detail="Link already exists.")

    new_link = models.Link(
        long_link = link.long_link
    )

    db.add(new_link)
    db.commit()

    id = new_link.id
    long_link = new_link.long_link
    print(f"Added new link: '{long_link}' (id : {id})")

    db.refresh(new_link)
    return new_link
