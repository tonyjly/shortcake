from sqlalchemy.orm import Session
from pydantic import HttpUrl
import string
import random
import models
import schemas

def create_link(link: HttpUrl, db: Session, new_short_link: str):
    """Create a new link and add to db
    """
    # Check if target link already exists
    db_link = db.query(models.Link).filter(models.Link.long_link==link.long_link).first()

    if db_link is not None:
        db_link = db.query(models.ShortLink).filter(models.ShortLink.id==db_link.short_link_id).first()
        return {
            "Status": "Link already exists.",
            "Original link": db_link.long_link,
            "Short link": "http://127.0.0.1:8000/" + new_short_link.short_link_path
        }

    new_link = models.Link(
        long_link = link.long_link,
        short_link_id = new_short_link.id
    )

    db.add(new_link)
    db.commit()
    db.refresh(new_link)
    return new_link

def create_short_link(db: Session, link: schemas.ShortLink):
    """Create and add a new short link
    """
    chars = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(chars) for i in range(8))

    new_short_link = models.ShortLink(
        short_link_path = random_string
    )

    # Check if short_link exists
    db_link = db.query(models.ShortLink).filter(models.ShortLink.short_link_path==new_short_link.short_link_path).first()

    if db_link is not None:
        new_short_link.short_link_path = ''.join(random.choice(chars) for i in range(8))

    db.add(new_short_link)
    db.commit()
    db.refresh(new_short_link)
    return new_short_link
