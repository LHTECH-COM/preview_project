from accounts import Accounts, API_URL
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

    def json(self):
        return self.json_data


# This method will be used by the mock to replace requests.get
def mocked_request_get_returns_response_data(*args, **kwargs):
    if args[0] == API_URL:
        return MockResponse({"id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
          "street": "Kulas Light",
          "suite": "Apt. 556",
          "city": "Gwenborough",
          "zipcode": "92998-3874",
          "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
          }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
          "name": "Romaguera-Crona",
          "catchPhrase": "Multi-layered client-server neural-net",
          "bs": "harness real-time e-markets"
        }}, 200)

    return MockResponse(None, 404)

def mock_request_get_returns_with_500_error_code(*args, **kwargs):
    if args[0] == API_URL:
        return MockResponse(None, 500)
    
class TestAcounts(unittest.TestCase):
    @mock.patch('requests.get', side_effect=mocked_request_get_returns_response_data)
    def test_get_api_success(self, mock_get):
        ac = Accounts()
        ac.get_api_account_list()
        self.assertIsNotNone(ac.accounts)
        

    @mock.patch('requests.get', side_effect=mock_request_get_returns_with_500_error_code)
    def test_get_api_fail(self, mock_get):
        ac = Accounts()
        with self.assertRaises(requests.exceptions.HTTPError):
            ac.get_api_account_list()


if __name__ == '__main__':
    unittest.main()
    
    