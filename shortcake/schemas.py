# from typing import Optional
from datetime import date
from pydantic import BaseModel

class Link(BaseModel):
    long_link: str

    class Config:
        orm_mode = True

class ShortLink(BaseModel):
    url: str
    date_created: date

    class Config:
        orm_mode = True
