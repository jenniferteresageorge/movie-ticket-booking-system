import unittest
from unittest.mock import patch
from controllers.movie_controller import create_movie, get_movie, get_movies, update_movie, delete_movie
from app import app, db

# Define a test class for Movie-related tests
class TestMovieController(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # Test case for retrieving all movies
    @patch("controllers.movie_controller.get_movies")
    def test_get_movies(self, mock_get_movies):
        # Call the get_movies function
        with self.client:
            response = self.client.get('/movies')
            movies = response.json

        # Assert that the result is a list
        self.assertIsInstance(movies, list)

    # Test case for retrieving a specific movie
    @patch("controllers.movie_controller.get_movie")
    def test_get_movie(self, mock_get_movie):
        # Call the get_movie function with a known movie ID
        movie = get_movie(movie_id=1)

        with self.client:
            response = self.client.get('/movies/1')
            movie = response.json

        # Assert that the result is not None
        self.assertIsNotNone(movie)
    
    @patch("controllers.movie_controller.session")
    # Test case for creating a new movie
    def test_create_movie(self, mock_session):
        mock_session.add.return_value = None
        mock_session.commit.return_value = None

        # Define movie data for creating a new movie
        movie_data = {
            'title': 'Test Movie',
            'director': 'Test Director',
            'genre': 'Test Genre',
            'release_date': '2024-04-20',
            'duration': 120,
            'synopsis': 'Test Synopsis'
        }

        # Call the create_movie function
        with self.client:
            response = self.client.post('/movies', json=movie_data)
            new_movie = response.json

        # Assert that the returned movie object is not None
        self.assertIsNotNone(new_movie)

        # Assert that the title of the created movie matches the expected title
        self.assertEqual(new_movie['title'], 'Test Movie')

    # Test case for updating an existing movie
    @patch("controllers.movie_controller.session")
    def test_update_movie(self, mock_session):
        mock_session.commit.return_value = None

        # Define updated movie data
        updated_movie_data = {
            'title': 'Updated Test Movie',
            'director': 'Updated Test Director',
            'genre': 'Updated Test Genre',
            'release_date': '2024-04-21',
            'duration': 130,
            'synopsis': 'Updated Test Synopsis'
        }

        # Call the update_movie function with a known movie ID and the updated data
        with self.client:
            response = self.client.put('/movies/1', json=updated_movie_data)
            updated_movie = response.json

        # Assert that the returned movie object is not None
        self.assertIsNotNone(updated_movie)

        # Assert that the title of the updated movie matches the expected updated title
        self.assertEqual(updated_movie['title'], 'Updated Test Movie')

    # Test case for deleting an existing movie
    @patch("controllers.movie_controller.session")
    def test_delete_movie(self, mock_session):
        mock_session.commit.return_value = None

        # Call the delete_movie function with a known movie ID
        with self.client:
            response = self.client.delete('/movies/1')

        # Assert that the status code indicates successful deletion
        self.assertEqual(response.status_code, 250)

        # Call the get_movie function with a known movie ID
        with self.client:
            response = self.client.get('/movies/1')
            deleted_movie = response.json

        # Assert that the result is None, indicating that the movie was deleted
        self.assertIsNone(deleted_movie)

# Run the tests if this file is executed directly
if __name__ == '__main__':
    unittest.main()
