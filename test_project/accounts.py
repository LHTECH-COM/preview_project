import csv
import json
import base64

ID_INDEX = 0
USER_NAME_INDEX = 1
PWD_INDEX = 2
FULL_NAME_INDEX = 3

class Accounts(object):
    '''
        A class is represent a user
        
        Attribues
        ------------------------
        id: int
            id of user
        user_name: str
            user name of user
        password: str
            password of user
        full_name: str
            full name of user
        pwd_encode: str
            encode pwd with base64
            
        Methods
        ---------------
        get_pwd_encode():
            return password encode with base64
    '''
    
    def __init__(self, user_info):
        self.id = user_info[ID_INDEX]
        self.user_name = user_info[USER_NAME_INDEX]
        self.password = user_info[PWD_INDEX]
        self.full_name = user_info[FULL_NAME_INDEX]
        self.pwd_encode = ""
        
    def get_pwd_encode(self):
        """
            return password encode with base64
        """
        if self.password:
            self.pwd_encode = base64.b64encode(bytes(self.password,"utf-8")).decode("utf-8")
        return self.pwd_encode

class RegisterAccount(object):
    '''
        A class to register account of user
        
        Attributes
        -------------------------
        total_num_row: int
            total num of row read from csv file
        accounts: array of string
            return list of data read from csv file
            
        Methods
        ---------------------------
        read_data_from_csv_file(): void
            read all data from csv file
        get_list_data(): object
            return list of all data read from csv file
        get_list_data_with_full_name_start_with(): object
            return list of data start with letter
    '''
    
    def __init__(self):
        self.total_num_row = 0
        self.accounts = []
        
    def read_data_from_csv_file(self, file_name):
        """
            read data from csv file
            arguments:
                file_name: path and name of file to read
        """
        try:
            print("begin read data from csv file")
            with open(file_name, "r") as file:
                reader = csv.reader(file, delimiter=",")
                for index, row_data in enumerate(reader):
                    if index == 0:
                        continue
                    else:
                        self.accounts.append(Accounts(row_data))
                        self.total_num_row +=1
            print("read data from csv file successfully")
        except FileNotFoundError as file_err:
            print("read data from csv file fail")
            raise
            
            
    def get_list_data(self, is_encoding = False):
        """
            get list of data read from csv file
            Arguments:
                is_encoding: encoding password or not
        """
        return json.dumps({
            "total_num_row": self.total_num_row,
            "new_accounts":[
                {
                    "id": account.id,
                    "user_name": account.user_name,
                    "password": account.password if not is_encoding else account.get_pwd_encode(),
                    "full_name": account.full_name
                } for account in self.accounts
                ]
            })
        
    def get_list_data_with_full_name_start_with(self, prefix_value=""):
        """
            get list of data read from csv file
            Arguments:
                prefix_value: prefix value want to filter
        """
        data_filter = filter(lambda x: x.full_name.startswith(prefix_value.lower()) or x.full_name.startswith(prefix_value.upper()), self.accounts)
        return json.dumps({
            "total_num_row": self.total_num_row,
            "new_accounts":[
                {
                    "id": account.id,
                    "user_name": account.user_name,
                    "password": account.get_pwd_encode(),
                    "full_name": account.full_name
                } for account in data_filter
                ]
            })
        
                
            
if __name__ == "__main__":
    ra = RegisterAccount()
    print("read data from csv file")
    ra.read_data_from_csv_file("MOCK_DATA.csv")
    print("list data read from csv file")
    print(ra.get_list_data())
    print("List data with encode base 64 password")
    print(ra.get_list_data(is_encoding=True))
    print("List data start with full name start with a")
    print(ra.get_list_data_with_full_name_start_with(prefix_value="a"))
    print(ra.get_list_data_test())
            
    
    
    
    
    
    
    
    
    
    
    