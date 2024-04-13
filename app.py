from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from controllers.movie_controller import get_movies, get_movie, create_movie, update_movie, delete_movie
from controllers.theater_controller import get_theaters, get_theater, create_theater, update_theater, delete_theater
from controllers.showtime_controller import get_showtimes, get_showtime, create_showtime, update_showtime, delete_showtime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie_ticket_booking.db'  # Adjust the database URI as per your setup

db = SQLAlchemy(app)

# Define API endpoints for movie CRUD operations
@app.route('/movies', methods=['GET'])
# Function to retrieve all movies
def get_all_movies():
    return jsonify(get_movies())

@app.route('/movies/<int:movie_id>', methods=['GET'])
# Function to retrieve a specific movie by ID
def get_single_movie(movie_id):
    return jsonify(get_movie(movie_id))
   
@app.route('/movies', methods=['POST'])
# Function to create a new movie
def add_movie():
    movie_data = request.json 
    return jsonify(create_movie(movie_data))
    

@app.route('/movies/<int:movie_id>', methods=['PUT'])
# Function to update an existing movie
def update_single_movie(movie_id):
    updated_movie_data = request.json
    return jsonify(update_movie(movie_id))
       
@app.route('/movies/<int:movie_id>', methods=['DELETE'])
# Function to delete an existing movie
def delete_single_movie(movie_id):
    return jsonify(delete_movie(movie_id))



# Define routes for theater CRUD operations
@app.route('/theaters', methods=['GET'])
def get_all_theaters():
    return jsonify(get_theaters())

@app.route('/theaters/<int:theater_id>', methods=['GET'])
def get_single_theater(theater_id):
    return jsonify(get_theater(theater_id))

@app.route('/theaters', methods=['POST'])
def add_theater():
    theater_data = request.json
    return jsonify(create_theater(theater_data))

@app.route('/theaters/<int:theater_id>', methods=['PUT'])
def update_single_theater(theater_id):
    updated_theater_data = request.json
    return jsonify(update_theater(theater_id))

@app.route('/theaters/<int:theater_id>', methods=['DELETE'])
def delete_single_theater(theater_id):
    return jsonify(delete_theater(theater_id))


# Define routes for showtime CRUD operations
@app.route('/showtimes', methods=['GET'])
def get_all_showtimes():
    return jsonify(get_showtimes())

@app.route('/showtimes/<int:showtime_id>', methods=['GET'])
def get_single_showtime(showtime_id):
    return jsonify(get_showtime(showtime_id))

@app.route('/showtimes', methods=['POST'])
def add_showtime():
    showtime_data = request.json
    return jsonify(create_showtime(showtime_data))

@app.route('/showtimes/<int:showtime_id>', methods=['PUT'])
def update_single_showtime(showtime_id):
    updated_showtime_data = request.json
    return jsonify(update_showtime(showtime_id))

@app.route('/showtimes/<int:showtime_id>', methods=['DELETE'])
def delete_single_showtime(showtime_id):
    return jsonify(delete_showtime(showtime_id))
 
if __name__ == '__main__':
    app.run(debug=True)
