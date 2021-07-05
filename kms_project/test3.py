import csv
import json
import requests

FIRST_NAME_INDEX = 0
LAST_NAME_INDEX = 1
IP_ADDRESS_INDEX = 2
API_URL = "https://httpbin.org/uuid"


class Users(object):
    """
    A class used to represent an user
    
    Attributes
    -----------------
    first_name: str
        first name of user
    last_name: str
        last name of user
    ip_address: str
        ip address of user
    uuid: str
        uuid of user
        
    Methods:
    ----------------
    get_uuid():
        get uuid from api
    """
    
    def __init__(self, user_info):
        """
        Parameters:
        --------------------
        user_info: array of string
            row data read from csv file
        """
        self.first_name = user_info[FIRST_NAME_INDEX]
        self.last_name = user_info[LAST_NAME_INDEX]
        self.ip_address = user_info[IP_ADDRESS_INDEX]
        self.uuid = ""
        
    def get_uuid(self):
        """
        get uuid from api
        
        returns:
        ---------------
        uuid: str
            uuid get from api
        """
        if not self.uuid:
            
            try:
                response = requests.get(API_URL)
                if response.status_code == 200:
                    data = response.json()
                    self.uuid = data["uuid"]
                else:
                    response.raise_for_status()
            except requests.exceptions.HTTPError as htt_err:
                print (htt_err)
            except requests.exceptions.ConnectionError as htt_err:
                print (htt_err)
            except requests.exceptions.Timeout as htt_err:
                print (htt_err)
            except requests.exceptions.RequestException as htt_err:
                print (htt_err)
        return self.uuid
class ReadUsers(object):
    """
    A class to read data from csv file and save to Users object
    
    Attributes
    --------------------------
    users_list: array of string
        return list of user read from csv file
        
    Methods
    ------------------------
    read_data_from_csv_file():
        read data from csv file
    get_list_data():
        return list of user read from csv file
    get_ipaddress_not_null()
        return list of user with ip address not null
    write_data_to_csv_file():
        write data to csv file
    """
    
    def __init__(self):
        """
        contains array list of users read from csv file
        """
        self.users_list = []
    
    
    def read_data_from_csv_file(self, file_name):
        """
        Read data from csv file
        
        Arguments
        -----------------
        file_name: str
            the file location of csv file
        """
        try:
            print("Begin read csv file")
            with open(file_name, "r") as file:
                reader = csv.reader(file, delimiter=",")
                for index, row_data in enumerate(reader):
                    if index == 0:
                        continue
                    else:
                        self.users_list.append(Users(row_data))
            print("write data to csv file successfully")
        except EOFError as err:
            print("read data from csv file fail")
    
    
    def get_list_data(self, is_sort_last_name = False):
        """
        return list of user read from csv file
        
        arguments
        ------------------
        is_sort_last_name: bool
            sort by last name or not
        """
        if is_sort_last_name:
            self.users_list.sort(key=lambda x:x.last_name, reverse=True)
        
        
        return [json.dumps({
                "first_name": user.first_name,
                "last_name":user.last_name,
                "ip_address":user.ip_address
            }) for user in self.users_list]
    
    
    def get_ipaddress_not_null(self):
        """
            return list of user with ip address not null
        """
        data_filter = [x for x in self.users_list if x.ip_address != ""]
        return [json.dumps({
                "first_name": user.first_name,
                "last_name":user.last_name,
                "ip_address":user.ip_address
            }) for user in data_filter]
        
    
    def write_data_to_csv_file(self):
        """
            write data to csv file
        """    
        try:
            print("begin write data to csv file")
            with open("test3_new.csv", mode="w") as csv_file:
                writer = csv.writer(csv_file, delimiter=",")
                writer.writerow(["uuid", "first_name","last_name","ip_address"])
                for data in self.users_list:
                    writer.writerow([data.get_uuid(), data.first_name, data.last_name, data.ip_address])
            print("write data to csv file successfully")
        except EOFError as err:
            print("write data to csv file fail")
    
if __name__ == "__main__":
    re = ReadUsers()
    re.read_data_from_csv_file("test3.csv")
    print("list of user read from csv file")
    print(re.get_list_data())
    print("sort by last name desc")
    print(re.get_list_data(is_sort_last_name=True))
    print(re.get_ipaddress_not_null())
    re.write_data_to_csv_file()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    