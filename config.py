# config.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib.parse

DB_USERNAME = 'root'
DB_PASSWORD = '1%40Kenneth2'
DB_HOST = 'localhost'
DB_PORT = 3306  # Default MySQL port
DB_NAME = 'movie_ticket_booking'
 
# URL encode the password
encoded_password = urllib.parse.quote_plus(DB_PASSWORD)
# Create the SQLAlchemy engine
DB_URI = f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DB_URI)

# Create a sessionmaker to interact with the database
Session = sessionmaker(bind=engine)
session = Session()