import requests
import csv
import json

API_URL = "https://httpbin.org/base64/"


class Data(object):
    """
        A class to read data from csv file
        
        Attributes
        ---------------------
        data_list: array of string
            data read from csv file
            
            
        Methods
        -------------------------
        read_data_from_csv_file(): void
            read all data from csv file
        decode_data():
            return value after decode from api
        get_list_data():
            return list of data read from csv file as json format
        write_data_to_csv_file(): void
            write data decode successful to csv file
    """
    
    def __init__(self):
        self.data_list = []
        self.data_decode_list = []
        
    def decode_data(self, value):
        """
            decode data with base64
            arguments:
                value: value want to decode
        """
        response_data = ""
        if value:
            try:
                api_path = f'{API_URL}{value}'
                response = requests.get(api_path)
                if response.status_code == 200:
                    response_data = response.text
                    
                else:
                    response.raise_for_status()
            except requests.HTTPError as http_err:
                print (http_err)
            except requests.ConnectionError as conn_err:
                print (conn_err)
            except requests.Timeout as tim_err:
                print (tim_err)
            except requests.RequestException as req_err:
                print (req_err)
        return response_data
        
    def read_data_from_csv_file(self, file_name):
        """
            read data from csv file
            arguments:
                file_name: path and file name of csv file
            
        """
        try:
            print("begin read data from csv file")
            with open(file_name, "r") as file:
                reader = csv.reader(file, delimiter=",")
                for index, row in enumerate(reader):
                    self.data_list.append(row[0])
                    self.data_decode_list.append(self.decode_data(row[0]))
            
            print ("read data to csv file successfully")
        except EOFError as err:
            print ("read data from csv file fail")
            
    def get_list_data(self):
        """
            list of data read from csv file and decode with base64 from api
        """
        return [{
                "decode_value": da
            } for da in self.data_decode_list]
            
    def write_data_to_csv_file(self):
        """
            write data decode successful to csv file
        """
        data_write = []
        data_list = self.data_decode_list
        for data in data_list:
            if "Incorrect Base64 data try" not in data:
                data_write.append(data)
        
        
        try:
            with open("data_new.csv", mode="w") as csv_file:
                writer = csv.writer(csv_file, delimiter=",")
                for da in data_write:
                    writer.writerow([da])
                    
            print ("write data to csv file successfully")
            
        except EOFError as err:
            print (err)
            
da = Data()
da.read_data_from_csv_file("data.csv")

print(da.get_list_data())
da.write_data_to_csv_file()


