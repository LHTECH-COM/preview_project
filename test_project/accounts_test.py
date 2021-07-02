from accounts import RegisterAccount
import unittest
import json

class TestRegisterAccount(unittest.TestCase):
    def test_read_data_from_csv_file_success(self):
        ra = RegisterAccount()
        ra.read_data_from_csv_file("MOCK_DATA.csv")
        self.assertNotEqual(ra.total_num_row, 0)
        
    def test_read_data_from_csv_file_fail(self):
        ra = RegisterAccount()
        with self.assertRaises(FileNotFoundError):
            ra.read_data_from_csv_file("")
            
    def test_get_list_data_succesful(self):
        ra = RegisterAccount()
        ra.read_data_from_csv_file("MOCK_DATA.csv")
        result = json.loads(ra.get_list_data())
        self.assertEqual(result["total_num_row"], 50)
        
        
if __name__ == "__main__":
    unittest.main()