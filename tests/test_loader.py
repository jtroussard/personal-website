import unittest
from unittest.mock import Mock, patch
from personal_website.content.loaders import ContentLoader

class TestContentLoader(unittest.TestCase):

    def setUp(self):
        # Create a mock logger
        self.logger = Mock()

        # Create a mock app configuration
        self.app_config = {
            "ENVIRONMENT": "test",
            "BUCKET_NAME": "test-bucket",
            "KAGIS": "test-key.json"
        }

        # Create an instance of ContentLoader
        self.content_loader = ContentLoader(self.app_config, self.logger)

    @patch('personal_website.content.loaders.signed_url_generator')
    def test_generate_signed_url(self, mock_signed_url_generator):
        mock_signed_url_generator.return_value = "https://example.com/test.json"
        file_name = "test.json"
        sub_bucket = "content"
        signed_url = self.content_loader.generate_signed_url(file_name, sub_bucket)
        self.assertEqual(signed_url, "https://example.com/test.json")

    @patch('personal_website.content.loaders.requests.get')
    def test_load_json(self, mock_requests_get):
        json_data = {"key": "value"}
        mock_requests_get.return_value.json.return_value = json_data
        self.content_loader.generate_signed_url = Mock(return_value="https://example.com/test.json")
        
        result = self.content_loader.load_json("test.json")
        self.assertEqual(result, json_data)

    @patch('personal_website.content.loaders.requests.get')
    def test_load_css(self, mock_requests_get):
        css_data = "body { background-color: white; }"
        mock_requests_get.return_value.text = css_data
        self.content_loader.generate_signed_url = Mock(return_value="https://example.com/test.css")
        
        result = self.content_loader.load_css("test.css")
        self.assertEqual(result, css_data)

    @patch('personal_website.content.loaders.requests.get')
    def test_load_image(self, mock_requests_get):
        image_data = b"\x89PNG\r\n\x1a\n\x00\x00"
        mock_requests_get.return_value.content = image_data
        self.content_loader.generate_signed_url = Mock(return_value="https://example.com/test.png")
        
        result = self.content_loader.load_image("test.png")
        self.assertEqual(result, image_data)

if __name__ == '__main__':
    unittest.main()
