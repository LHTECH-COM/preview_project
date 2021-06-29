from account import RegisterAccount
import unittest
import json


class TestRegisterAccount(unittest.TestCase):
    def test_read_csv_file_success(self):
        ra = RegisterAccount()
        ra.read_data_from_csv_file("MOCK_DATA.csv")
        self.assertNotEqual(ra.total_row, 0)
    
    
    def test_read_csv_file_fail(self):
        ra = RegisterAccount()
        with self.assertRaises(FileNotFoundError):
            ra.read_data_from_csv_file("")
            
            
    def test_return_list_data_pwd_encode(self):
        ra = RegisterAccount()
        ra.read_data_from_csv_file("MOCK_DATA.csv")
        ra.get_list_data_encode_pwd_base64()
        self.assertNotEqual(ra.total_row, 0)
        
        
if __name__ == "_main__":
    unittest.main()
        