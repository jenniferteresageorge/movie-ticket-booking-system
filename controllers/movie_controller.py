from flask import Flask, jsonify, request
from models.movie import Movie
from models.showtime import Showtime
from models.theater import Theater
from config import session

app = Flask(__name__)

# Define API endpoints for movie CRUD operations
@app.route('/movies', methods=['GET'])
# Function to retrieve all movies
def get_movies():
    movies = session.query(Movie).all()
    return jsonify([movie.__dict__ for movie in movies])

@app.route('/movies/<int:movie_id>', methods=['GET'])
# Function to retrieve a specific movie by ID
def get_movie(movie_id):
    movie = session.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        return jsonify(movie.serialize())
    else:
        return jsonify(message="Movie not found"), 404

@app.route('/movies', methods=['POST'])
# Function to create a new movie
def create_movie(movie_data):
    movie_data = request.json 
    if movie_data:
       movie = Movie(**movie_data)
       session.add(movie)
       session.commit()
       return jsonify(movie.serialize()), 201
    else:
        return jsonify(message="Invalid movie data"), 400

@app.route('/movies/<int:movie_id>', methods=['PUT'])
# Function to update an existing movie
def update_movie(movie_id):
    updated_movie_data = request.json
    if updated_movie_data:
        movie = session.query(Movie).filter(Movie.id == movie_id).first()
        if movie:
            for key, value in updated_movie_data.items():
                setattr(movie, key, value)
            session.commit()
            return jsonify(movie.serialize())
        else:
            return jsonify(message="Movie not found"), 404
    else:
        return jsonify(message="Invalid movie data"), 400

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
# Function to delete an existing movie
def delete_movie(movie_id):
    movie = session.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        session.delete(movie)
        session.commit()
        return jsonify(message="Movie deleted"), 200
    else:
        return jsonify(message="Movie not found"), 404

if __name__ == '__main__':
    app.run(debug=True)

print("Script executed successfully.")
