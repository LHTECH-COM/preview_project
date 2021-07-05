import requests
import json
import csv 

class Data(object):
    """
    A class to save data read from csv file
    
    Attribues:
    -------------------
    data_list: array of string
        list of data read from csv file
            
    Methods:
    ----------------------
    read_data_from_csv_file(file_name):
        read data from csv file
    decode_base64():
        return list data with decode base64
    get_list_data_decode():
        return list data decode base64
    """
    
    def __init__(self):
        """
        data and data decode read from csv file
        """
        self.data_list = []
        self.data_decode = []
    
    def read_data_from_csv_file(self, file_name):
        """
        read data from csv file
        arguments:
        --------------------------
        file_name: str
            the file location of csv file
        """
        try:
            with open(file_name, "r") as file:
                reader = csv.reader(file, delimiter=",")
                for index, row in enumerate(reader):
                    self.data_list.append(row[0])
                    
            print("read data from csv file successfully")
        except IOError as err:
            print("read data from csv file fail")
            
            
    def decode_base64(self, value):
        """
        decode value with base64 from api
        
        Parameters:
        -------------------
        value: str
            value to decode
        
        Returns:
        -----------------
        string
            string decode from base64
        """
        try:
            api_url = f"https://httpbin.org/base64/{value}"
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.text
                return data
            else:
                response.raise_for_status()
        except requests.exceptions.HTTPError as htt_err:
            print(htt_err)
        except requests.exceptions.ConnectionError as htt_err:
            print(htt_err)
        except requests.exceptions.Timeout as htt_err:
            print(htt_err)
        except requests.exceptions.RequestException as htt_err:
            print(htt_err)
            
    def get_list_data_decode(self):
        """
        get list data decode with base64
        """
        self.data_decode = list(self.decode_base64(data) for data in self.data_list)
        
    def get_list_data(self, is_success = False):
        """
        get list data decode with base64
        
        arguments:
        -------------------------
        is_success: bool, optional
            decode with base64 success or not, default is all data decode
        """
        data_decode = self.data_decode
        if is_success:
            data_decode = [data for data in self.data_decode if "Incorrect Base64 data try" not in data]
        return [json.dumps({
            "data_decode": data
            }) for data in data_decode]
            
            
if __name__ == "__main__":
    da = Data()
    da.read_data_from_csv_file("test5.csv")
    da.get_list_data_decode()
    print("get list data with decode base 64")
    
    print(da.get_list_data())
    print("get list data decode successfully")
    print(da.get_list_data(True))
            
            
            
            