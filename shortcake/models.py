from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from db import Base

class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    long_link = Column(String, unique=True, nullable=False, index=True)
    short_link_id = Column(ForeignKey("short_links.id"), nullable=False)


class ShortLink(Base):
    __tablename__ = "short_links"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    short_link_path = Column(String, unique=True, nullable=False, index=True)
