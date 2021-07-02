import requests
import json
import csv

API_URL = "https://httpbin.org/base64/"


class Data(object):
    """
         A class save string data with base64
         
         Attributes
         ------------------
         data_list: array of string
              
        Methods
        ------------------------
        read_data_from_csv_file(): void
            read data from csv file
        get_list_data(): object
            return list of data read from csv file
        decode_base64(): 
        return data decode with base64 from api
    """
    #array of string read from csv file
    
    def __init__(self):
        self.data_list = []
    
        
    def read_data_from_csv_file(self, file_name):
        """
            read data from csv file
            Arguments:
                file_name: path and file name of csv file
        """
        try:
            with open(file_name, "r") as file:
                reader = csv.reader(file, delimiter=",")
                for index, row in enumerate(reader):
                    self.data_list.append(row[0])
                     
            print("Read data from csv file sucessfully")
        except IOError as io_err:
            print (io_err)
            print("read data from csv file fail")
            
            
    def get_list_data(self):
        """
            list data read from csv file as json format
        """
        
        return json.dumps([{
            "row_data": self.decode_base64(row)
            } for row in self.data_list])
    
    def decode_base64(self, value):
        """
            decode data with base64
        """
        try:
            api_link = f'{API_URL}{value}'
            
            response = requests.get(api_link)
            if response.status_code == 200:
                response_data = response.text
                return response_data
            else:
                response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print (http_err)
        except requests.exceptions.ConnectionError as conn_err:
            print (conn_err)
        except requests.exceptions.Timeout as tim_err:
            print (tim_err)
        except requests.exceptions.RequestException as req_err:
            print (req_err)
            
            
if __name__ == "__main__":
    da = Data()
    #read data from csv file
    da.read_data_from_csv_file("data.csv")
    #get list data from csv file
    print(da.get_list_data())
    
    
    
            
            
        