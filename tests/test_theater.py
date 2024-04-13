import unittest
from unittest.mock import patch, MagicMock
from controllers.theater_controller import get_theaters, get_theater, create_theater, update_theater, delete_theater

# Define a test class for Theater-related tests
class TestTheaterController(unittest.TestCase):
    # Test case for retrieving all theaters
    def test_get_theaters(self):

        # Call the get_theaters function
        theaters = get_theaters()

        # Assert that the result is a list
        self.assertIsInstance(theaters, list)

    @patch('controllers.theater_controller.get_theater')
    def test_get_theater(self, mock_get_theater):
    # Mock the behavior of get_theater function to return None
        mock_get_theater.return_value = None

    # Call the get_theater function
        theater = get_theater(1)

    # Assert that the result is None
        self.assertIsNone(theater)

    # Mock the behavior of get_theater function to return theater data
        mock_get_theater.return_value = {'id': 1, 'name': 'Test Theater', 'location': 'Test Location', 'capacity': 100}

    # Call the get_theater function
        theater = get_theater(1)

    # Assert that the returned theater object has 'name' attribute
        self.assertTrue(hasattr(theater, 'name'))
    # Test case for creating a new theater
    def test_create_theater(self):
        # Define theater data for creating a new theater
        theater_data = {
            'name': 'Test Theater',
            'location': 'Test Location',
            'capacity': 100
        }

        # Call the create_theater function
        new_theater = create_theater(theater_data)

        # Assert that the returned theater object is not None
        self.assertIsNotNone(new_theater)
        # Assert that the 'name' attribute of the theater object matches the expected name
        self.assertEqual(new_theater.name, 'Test Theater')


    # Test case for updating an existing theater
    @patch('controllers.theater_controller.update_theater')
    def test_update_theater(self, mock_update_theater):
        # Define updated theater data
        updated_theater_data = {
            'name': 'Updated Test Theater',
            'location': 'Updated Test Location',
            'capacity': 150
        }

        # Mock the update_theater function to return None
        mock_update_theater.return_value = None

        # Call the update_theater function with a known theater ID and the updated data
        updated_theater = update_theater(1, updated_theater_data)

        # Assert that the updated_theater is None
        self.assertIsNone(updated_theater)

        # Mock the update_theater function to return updated theater data
        mock_update_theater.return_value = updated_theater_data

        # Call the update_theater function with a known theater ID and the updated data
        updated_theater = update_theater(1, updated_theater_data)

        # Assert that the updated theater data matches the expected updated data
        self.assertEqual(updated_theater['name'], 'Updated Test Theater')

    # Test case for deleting an existing theater
    @patch('controllers.theater_controller.delete_theater')
    def test_delete_theater(self, mock_delete_theater):
        # Call the delete_theater function with a known theater ID
        delete_theater(1)

        # Call the get_theater function with the same theater ID
        deleted_theater = get_theater(1)

        # Assert that the result is None, indicating that the theater was deleted
        mock_delete_theater.assert_called_with(1)

# Run the tests if this file is executed directly
if __name__ == '__main__':
    unittest.main()


