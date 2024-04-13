import unittest
from unittest.mock import patch, MagicMock
from controllers.showtime_controller import get_showtimes, get_showtime, create_showtime, update_showtime, delete_showtime

class TestShowtimeController(unittest.TestCase):
    @patch("controllers.showtime_controller.session")
    def test_get_showtimes(self, mock_session):
        # Mock the query method of the session object to return a list of showtimes
        mock_session.query().all.return_value = [MagicMock(), MagicMock()]

        # Call the get_showtimes function
        showtimes = get_showtimes()

        # Assert that the result is a list
        self.assertIsInstance(showtimes, list)

    @patch("controllers.showtime_controller.session")
    def test_get_showtime(self, mock_session):
        # Mock the query method of the session object to return a showtime object
        mock_session.query().filter_by().first.return_value = MagicMock()

        # Call the get_showtime function with a known showtime ID
        showtime = get_showtime(1)

        # Assert that the result is not None
        self.assertIsNotNone(showtime)

    @patch("controllers.showtime_controller.session")
    def test_create_showtime(self, mock_session):
        # Define showtime data for creating a new showtime
        showtime_data = {
            'movie_id': 1,
            'theater_id': 1,
            'date_time': '2024-04-20 15:00:00',
            'available_seats': 100
        }

        # Call the create_showtime function
        new_showtime = create_showtime(showtime_data)

        # Assert that the returned showtime object is not None
        self.assertIsNotNone(new_showtime)

        # Assert that the movie ID of the created showtime matches the expected movie ID
        self.assertEqual(new_showtime.movie_id, 1)

    @patch("controllers.showtime_controller.session")
    def test_update_showtime(self, mock_session):
        # Define updated showtime data
        updated_showtime_data = {
            'date_time': '2024-04-20 16:00:00',
            'available_seats': 150
        }

        # Mock the query method of the session object to return a showtime object
        mock_session.query().filter_by().first.return_value = MagicMock()

        # Call the update_showtime function with a known showtime ID and the updated data
        updated_showtime = update_showtime(1, updated_showtime_data)

        # Assert that the returned showtime object is not None
        self.assertIsNotNone(updated_showtime)

        # Assert that the date_time of the updated showtime matches the expected updated date_time
        self.assertEqual(updated_showtime.date_time, '2024-04-20 16:00:00')

    @patch("controllers.showtime_controller.session")
    def test_delete_showtime(self, mock_session):

        # Call the delete_showtime function with a known showtime ID
        delete_showtime(1)
        mock_session.query().filter().first.return_value = None

        # Call the get_showtime function with the same showtime ID
        deleted_showtime = get_showtime(1)

        # Assert that the result is None, indicating that the showtime was deleted
        self.assertIsNone(deleted_showtime)

if __name__ == '__main__':
    unittest.main()
