from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Showtime(Base):
    __tablename__ = 'showtimes'

    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    theater_id = Column(Integer, ForeignKey('theaters.id'))
    date_time = Column(DateTime)
    available_seats = Column(Integer)

    movie = relationship("Movie", backref="showtimes")
    theater = relationship("Theater", backref="showtimes")

    def serialize(self):
        return {
            'id': self.id,
            'movie_id': self.movie_id,
            'theater_id': self.theater_id,
            'date_time': self.date_time,
            'available_seats': self.available_seats
            
        }
    def __init__(self, movie, theater, date_time, available_seats):
        self.movie = movie
        self.theater = theater
        self.date_time = date_time
        self.available_seats = available_seats