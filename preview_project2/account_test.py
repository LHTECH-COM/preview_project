from unittest import mock
from account import Account, API_URL
import unittest
import json
import requests

class MockResponse(requests.Response):
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code
        self.reason = ""
        self.url = ""

    def json(self):
        return self.json_data
    
def mocked_get_api_success(*args, **kwargs):
    if args[0]== API_URL:
        return MockResponse({"success":True, "uuid":"e21bf68f-2265-4863-8b91-517d8aa86043"},200)
    return MockResponse(None, 400)

def mocked_get_api_fail(*args, **kwargs):
    if args[0]== API_URL:
        return MockResponse(None, 500)
    
    
class TestRegisterAccount(unittest.TestCase):
    @mock.patch('requests.get', side_effect=mocked_get_api_success)
    def test_get_uuid_success(self, mock_get):
        row = {
            "first_name":"first_name",
            "last_name":"last_name",
            "ip_address":"ip_address"
            }
        
        ac = Account(row)
        result = ac.get_uuid()
        self.assertIsNotNone(result)
        
    @mock.patch('requests.get', side_effect=mocked_get_api_fail)
    def test_get_uuid_fail(self, mock_get):
        row = {
            "first_name":"first_name",
            "last_name":"last_name",
            "ip_address":"ip_address"
            }
        
        ac = Account(row)
        with self.assertRaises(requests.exceptions.HTTPError):
            ac.get_uuid()


if __name__ == "__main__":
    unittest.main()        
        