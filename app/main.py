from typing import List
from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from starlette.responses import RedirectResponse
from db import SessionLocal, Base, engine
import models, schemas, crud
import uvicorn
import os

API_IP = os.environ.get('API_IP')
API_PORT = os.environ.get('API_PORT')
API_ADDRESS = f"http://{API_IP}:{API_PORT}/"

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
    """Show random 25 long links upon entry
    """
    return crud.read_links(db=db)

@app.get("/links")
def read_links(db: Session = Depends(get_db)):
    """Show random 25 long links
    """
    return crud.read_links(db=db)

@app.get("/short-links", response_model=List[schemas.ShortLink])
def read_short_links(db: Session = Depends(get_db)):
    short_links = db.query(models.ShortLink).order_by(func.random()).limit(25).all()
    return short_links

@app.post("/add-link")
def add_link(link: schemas.Link, db: Session = Depends(get_db)):
    """Create a new link and add to db
    """
    # Check if target link already exists
    db_link = db.query(models.Link).filter(models.Link.long_link==link.long_link).first()

    if db_link is not None:
        db_short_link = db.query(models.ShortLink).filter(models.ShortLink.id==db_link.short_link_id).first()
        return {
            "Status": "Link already exists.",
            "Original link": db_link.long_link,
            "Short link": API_ADDRESS + db_short_link.short_link_path
        }

    new_short_link = crud.create_short_link(db=db, link=link)
    new_link = crud.create_link(db=db, link=link, new_short_link=new_short_link)

    return {
        "Status": "Link successfully processed.",
        "Original link": new_link.long_link,
        "Short link": API_ADDRESS + new_short_link.short_link_path
    }

@app.get("/{short_link_path}", response_model=schemas.ShortLink)
def get_long_link(short_link_path: str, db: Session = Depends(get_db)):
    """Redirect to original link from short link
    """
    db_short_link = db.query(models.ShortLink).filter(models.ShortLink.short_link_path==short_link_path).first()
    short_link_id = db_short_link.id
    db_long_link = db.query(models.Link).filter(models.Link.short_link_id==short_link_id).first()
    long_link = db_long_link.long_link
    return RedirectResponse(url=long_link, status_code=302)
