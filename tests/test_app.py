import unittest
from personal_website import init_app

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = init_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
