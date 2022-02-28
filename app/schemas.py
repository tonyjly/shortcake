from pydantic import BaseModel, HttpUrl

class Link(BaseModel):
    long_link: HttpUrl

    class Config:
        orm_mode = True

class ShortLink(BaseModel):
    id: int
    short_link_path: str

    class Config:
        orm_mode = True
