from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    genre = Column(String)
    release_date = Column(Date)
    duration = Column(Integer)
    synopsis = Column(String)
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'director': self.director,
            'genre': self.genre,
            'release_date': self.release_date,
            'duration': self.duration,
            'synopsis': self.synopsis
        }

    def __init__(self, title, director, genre, release_date, duration, synopsis):
        self.title = title
        self.director = director
        self.genre = genre
        self.release_date = release_date
        self.duration = duration
        self.synopsis = synopsis

