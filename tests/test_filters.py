import os
import unittest
from unittest.mock import Mock
from personal_website import filters
from flask import Flask

class TestFilters(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.static_folder = os.path.join(os.path.dirname(__file__), 'static')
        filters.app = self.app

    def test_get_icon_url_existing_icon(self):
        with self.app.test_request_context():
            os.path.exists = Mock(return_value=True)

            input_string = "test"
            expected_url = "/static/images/icons/icons8-test-50.png"
            result = filters.get_icon_url(input_string)

            self.assertEqual(result, expected_url)

    def test_get_icon_url_non_existing_icon(self):
        with self.app.test_request_context():
            os.path.exists = Mock(return_value=False)

            input_string = "nonexistent"
            expected_url = "/static/images/icons/default-icon.png"
            result = filters.get_icon_url(input_string)

            self.assertEqual(result, expected_url)

if __name__ == '__main__':
    unittest.main()
