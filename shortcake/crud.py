from sqlalchemy.orm import Session
import string
import random
import models
import schemas


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
