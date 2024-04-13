from models.showtime import Showtime  # Import the Showtime model
from config import session  # Import the existing session object from config.py
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, jsonify, request

app = Flask(__name__)

Base = declarative_base()

class Showtime(Base):
    __tablename__ = 'showtimes'

    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, nullable=False)
    theater_id = Column(Integer, nullable=False)
    date_time = Column(DateTime, nullable=False)
    available_seats = Column(Integer, nullable=False)

# Function to retrieve all showtimes
@app.route('/showtimes', methods=['GET'])
def get_showtimes():
    showtimes = session.query(Showtime).all()
    return jsonify([showtime.serialize() for showtime in showtimes])


# Function to retrieve a specific showtime by ID
@app.route('/showtimes/<int:showtime_id>', methods=['GET'])
def get_showtime(showtime_id):
    showtime = session.query(Showtime).filter(Showtime.id == showtime_id).first()
    if showtime:
        return jsonify(showtime.serialize())
    else:
        return jsonify(message="Showtime not found"), 404


# Function to create a new showtime
@app.route('/showtimes', methods=['POST'])
def create_showtime():
    showtime_data = request.json 
    if showtime_data:
        showtime = Showtime(**showtime_data)
        session.add(showtime)
        session.commit()
        return jsonify(showtime.serialize()), 201
    else:
        return jsonify(message="Invalid showtime data"), 400
'''
    movie_id = showtime_data.get('movie_id')
    theater_id = showtime_data.get('theater_id')
    date_time = showtime_data.get('date_time')
    available_seats = showtime_data.get('available_seats')

    showtime = Showtime(
        movie_id=movie_id,
        theater_id=theater_id,
        date_time=date_time,
        available_seats=available_seats
    )
    session.add(showtime)
    session.commit()
    return showtime
'''
# Function to update an existing showtime
@app.route('/showtimes/<int:showtime_id>', methods=['PUT'])
def update_showtime(showtime_id):
    updated_showtime_data = request.json
    if updated_showtime_data:
        showtime = session.query(Showtime).filter(Showtime.id == showtime_id).first()
        if showtime:
            for key, value in updated_showtime_data.items():
                setattr(showtime, key, value)
            session.commit()
            return jsonify(showtime.serialize())
        else:
            return jsonify(message="Showtime not found"), 404
    else:
        return jsonify(message="Invalid showtime data"), 400

# Function to delete an existing showtime
@app.route('/showtimes/<int:showtime_id>', methods=['DELETE'])
def delete_showtime(showtime_id):
    showtime = session.query(Showtime).filter(Showtime.id == showtime_id).first()
    if showtime:
        session.delete(showtime)
        session.commit()
        return jsonify(message="Showtime deleted"), 200
    else:
        return jsonify(message="Showtime not found"), 404

if __name__ == '__main__':
    app.run(debug=True)
