import json
import csv
import requests

FIRST_NAME_INDEX = 0
LAST_NAME_INDEX = 1
IP_ADDRESS_INDEX = 2
API_URL = "https://httpbin.org/uuid"


class Account:
    """
    A class is represent user
    
    Attributes
    -------------------
    first_name: str
        first name of user
    last_name: str
        last name of user
    ip_address: str
        ip_address of user
        
    Methods
    ----------------
    get_uuid(): void
        return uuid get from api
    """
    
    def __init__(self, info):
        self.first_name = info["first_name"]
        self.last_name = info["last_name"]
        self.ip_address = info["ip_address"]
        self.uuid = ""
    
    #get uuid from web api
    def get_uuid(self):
        if not self.uuid:
            try:
                response = requests.get(API_URL)
                if response.status_code == 200:
                    response_data = response.json()
                    uuid = response_data["uuid"]
                    self.uuid = uuid
                else:
                    response.raise_for_status()
            except requests.exceptions.HTTPError as http_err:
                print (http_err)
                raise
            except requests.exceptions.ConnectionError as conn_err:
                #raise
                print (conn_err)
            except requests.exceptions.Timeout as tim_err:
                #raise
                print (tim_err)
            except requests.exceptions.RequestException as req_err:
                #raise
                print (req_err)
        return self.uuid
        
class RegisterAccount():
    """
    A class to register account of user
    
    Attributes
    ----------------------
    accounts: array of str
        list of all account
        
    Methods
    ---------------------
    read_csv_file(): void
        read all data from csv file
    get_list_data(): void
        return list all data read from csv file as json format
    get_list_data_sort_by_last_name_desc(): void
        return list of data sort by last name desc
    get_list_data_with_ip_address_not_null(): void
        return list of data with ip address not null
    write_data_to_csv_file(): void
        write list of data to csv file
    """
    
    def __init__(self):
        self.accounts = []
        
    #read data from csv file
    def read_csv_file(self, file_name):
        try:
            with open(file_name, "r") as file:
                reader = csv.reader(file, delimiter=",")
                for index, row_data in enumerate(reader):
                    if index == 0:
                        continue
                    else:
                        user_info = {
                            "first_name": row_data[FIRST_NAME_INDEX],
                            "last_name": row_data[LAST_NAME_INDEX],
                            "ip_address": row_data[IP_ADDRESS_INDEX]
                            }
                        self.accounts.append(Account(user_info))
            print ("read data from csv file successfully")
        except FileNotFoundError as file_err:
            raise
            print ("read data from csv file fail")
    
    #get list data read from csv file
    def get_list_data(self):
        return [json.dumps({
            "first_name":account.first_name,
            "last_name":account.last_name,
            "ip_address":account.ip_address
            }) for account in self.accounts]
    
    #list of data sort by last name desc
    def get_list_data_sort_by_last_name_desc(self):
        self.accounts.sort(key=lambda x: x.last_name, reverse=True)
        return [json.dumps({
            "first_name":account.first_name,
            "last_name":account.last_name,
            "ip_address":account.ip_address
            }) for account in self.accounts]
    
    #list of data with ipaddress not null
    def get_list_data_with_ip_address_not_null(self):
        data_filter = filter(lambda x: x.ip_address != "", self.accounts)
        return [json.dumps({
            "first_name":account.first_name,
            "last_name":account.last_name,
            "ip_address":account.ip_address
            }) for account in data_filter]
        
    #write data to csv file
    def write_data_to_csv_file(self):
        try:
            with open("data_new.csv", mode="w") as csv_file:
                writer = csv.writer(csv_file, delimiter=",")
                writer.writerow(["UUID","FIRT NAME", "LAST NAME", " IP ADDRESS"])
                for account in self.accounts:
                    writer.writerow([account.get_uuid(), account.first_name, account.last_name, account.ip_address])
            print ("write data to csv file successfully")
        except EOFError as er:
            print ("write data to csv file fail") 
        
        
    
if __name__ == "__main__":
    ra = RegisterAccount()
    #read data from csv file
    ra.read_csv_file("data.csv")
    #get list data from csv file
    print(ra.get_list_data())
    #get list of data sort by last name desc
    print(ra.get_list_data_sort_by_last_name_desc())
    #get list of data sort by ip address not null
    print (ra.get_list_data_with_ip_address_not_null())
    #write data to csv file
    ra.write_data_to_csv_file()
    
    
    