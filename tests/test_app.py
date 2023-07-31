import unittest
from personal_website import create_app

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        # Create a test client and use the app context
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_home_page(self):
        # Test if the home page ("/") loads without errors (HTTP status code 200)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_coming_soon_page(self):
        # Test if the coming-soon page ("/coming-soon") loads without errors (HTTP status code 200)
        response = self.client.get('/coming-soon')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
