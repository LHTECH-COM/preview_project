from data import Data
from unittest import mock
import unittest
import json
import requests

class MockResponse(requests.Response):
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code
        self.reason = ''
        self.url = ''
        self.encoding = ""
        self._content = ""

    def json(self):
        return self.json_data


# This method will be used by the mock to replace requests.get
def mocked_request_get_returns_response_data(*args, **kwargs):
    if args[0] == "https://httpbin.org/base64/cHl0aG9u":
        return MockResponse({"python"}, 200)

    return MockResponse(None, 404)

def mock_request_get_returns_with_500_error_code(*args, **kwargs):
    if args[0] == "https://httpbin.org/base64/cHl0aG9u":
        return MockResponse(None, 500)
    
class TestAcounts(unittest.TestCase):
    @mock.patch('requests.get', side_effect=mocked_request_get_returns_response_data)
    def test_get_api_success(self, mock_get):
        da = Data()
        result = da.decode_data("cHl0aG9u")
        self.assertIsNotNone(result)
        

    @mock.patch('requests.get', side_effect=mock_request_get_returns_with_500_error_code)
    def test_get_api_fail(self, mock_get):
        da = Data()
        with self.assertRaises(requests.exceptions.HTTPError):
            da.decode_data("cHl0aG9u")


if __name__ == '__main__':
    unittest.main()