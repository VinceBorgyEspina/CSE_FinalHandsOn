import unittest
from flask_testing import TestCase
from app import app, data_fetch, generate_xml_response

class TestYourFlaskApp(TestCase):
    
    def create_app(self):
        app.config['TESTING'] = True
        app.config["MYSQL_DB"] = "test_db"  # Use a separate test database
        return app

    def setUp(self):
        # Set up test data or any other preparations
        pass

    def tearDown(self):
        # Clean up after the test
        pass

    def test_data_fetch(self):
        # Test data_fetch function
        with app.app_context():
            # Assuming a valid query for testing purposes
            query = "SELECT * FROM mydb.athlete"
            response = data_fetch(query)
            self.assert200(response)  # Assuming a successful response code
            self.assertIn("athlete_id", response.json[0])  # Assuming athlete_id is in the response data

    def test_generate_xml_response(self):
        # Test generate_xml_response function
        data = [{"athlete_id": 1, "athlete_firstname": "John"}]
        response = generate_xml_response(data)
        self.assert200(response)
        self.assertIn(b"<athlete_id>1</athlete_id>", response.data)  # Assuming athlete_id is in the XML data

    def test_get_athlete_by_id(self):
        # Test the '/athlete/<int:id>' endpoint
        response = self.client.get('/athlete/1')
        self.assert200(response)
        self.assertEqual(response.content_type, 'application/json')

    def test_get_club(self):
        # Test the '/club' endpoint
        response = self.client.get('/club')
        self.assert200(response)
        self.assertEqual(response.content_type, 'application/json')

    def test_add_club(self):
        # Test the '/club' POST endpoint
        data = {
            "club_id": 1,
            "club_name": "Test Club",
            "club_location": "Test Location",
        }
        response = self.client.post('/club', json=data)
        self.assert201(response)
        self.assertIn("message", response.json)

    def test_update_club(self):
        # Test the '/club/<int:id>' PUT endpoint
        data = {
            "club_id": 1,
            "club_name": "Updated Club",
            "club_location": "Updated Location",
        }
        response = self.client.put('/club/1', json=data)
        self.assert200(response)
        self.assertIn("message", response.json)

    def test_delete_club(self):
        # Test the '/club/<int:id>' DELETE endpoint
        response = self.client.delete('/club/1')
        self.assert200(response)
        self.assertIn("message", response.json)

    def test_get_query_join(self):
        # Test the '/query_join' endpoint
        response = self.client.get('/query_join')
        self.assert200(response)
        self.assertEqual(response.content_type, 'application/json')

    def test_get_query_sort(self):
        # Test the '/query_sort' endpoint
        response = self.client.get('/query_sort')
        self.assert200(response)
        self.assertEqual(response.content_type, 'application/json')

    def test_get_query_group(self):
        # Test the '/query_group' endpoint
        response = self.client.get('/query_group')
        self.assert200(response)
        self.assertEqual(response.content_type, 'application/json')

if __name__ == '__main__':
    unittest.main()
