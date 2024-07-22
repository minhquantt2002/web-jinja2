import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.dialects.postgresql import TEXT
from .database import Base


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(255))
    content = Column(TEXT)
    image_url = Column(String(255))
    view = Column(Integer)
    created = Column(DateTime, default=datetime.datetime.now())


class Video(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    video_id = Column(String(255))
