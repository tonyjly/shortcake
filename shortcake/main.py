from typing import List # Optional,
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
import uvicorn

import models, schemas, crud
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
def read_links(db: Session = Depends(get_db)):
    links = db.query(models.Link).all()
    return links


@app.get("/short-links", response_model=List[schemas.ShortLink])
def read_short_links(db: Session = Depends(get_db)):
    short_links = db.query(models.ShortLink).all()
    return short_links


@app.post("/add-link", response_model=schemas.Link)
def create_link(link: schemas.Link, db: Session = Depends(get_db)):
    """Create a new link and add to db
    """
    # Check if target link already exists
    db_link = db.query(models.Link).filter(models.Link.long_link==link.long_link).first()

    if db_link is not None:
        # raise HTTPException(status_code=400, detail="Link already exists.")
        db_short_link = db.query(models.ShortLink).filter(models.ShortLink.id==db_link.short_link_id).first()
        return RedirectResponse(url=db_short_link.short_link, status_code=302)

    new_short_link = crud.create_short_link(db=db, link=link)

    new_link = models.Link(
        long_link = link.long_link,
        short_link_id = new_short_link.id
    )

    db.add(new_link)
    db.commit()
    db.refresh(new_link)
    return new_link

@app.get("/{short_link_path}", response_model=schemas.ShortLink)
def get_long_link(short_link_path: str, db: Session = Depends(get_db)):
    """Redirect to original link from short link
    """
    db_short_link = db.query(models.ShortLink).filter(models.ShortLink.short_link_path==short_link_path).first()
    short_link_id = db_short_link.id
    db_long_link = db.query(models.Link).filter(models.Link.short_link_id==short_link_id).first()
    long_link = db_long_link.long_link
    return RedirectResponse(url=long_link, status_code=302)
