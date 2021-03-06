import csv
import json
import base64


ID_INDEX = 0
USERNAME_INDEX = 1
PWD_INDEX = 2
FULL_NAME_INDEX = 3

class Account(object):
    
    """
    A class is represent account of user
    
    Attributes
    ---------------------------
    id: int
        id of user
    username: str
        username of user
    password: str
        password of user
    full_name: str
        full name of user
        
    Methods
    -----------------
    encode_pwd(): void
        encode pwd to base64
    """
    
    def __init__(self, info):
        self.id = info.get("id")
        self.username = info.get("username")
        self.password = info.get("password")
        self.full_name = info.get("full_name")
        self.pwd_encode  = ""
    
    
    def encode_pwd(self):
        """
            encode pwd
        """
        if self.password:
            pwd_encode =  base64.b64encode(bytes(self.password, 'utf-8')).decode("utf-8") 
            self.pwd_encode = f'{pwd_encode}'
        
        return self.pwd_encode
    
    
   
    
        
class RegisterAccount(object):
    """
    A class to register account of user read from csv file
    
    Attributes
    ----------------
    accounts: array of str
        list account of user
        
    Methods:
    -------------------
    read_data_from_csv_file(): void
        read all data from csv file
    get_list_data(): object
        return list of data read from csv file as json format
    get_list_data_encode_pwd_base64(): object
        return list of data with encode password base 64
    write_data_to_csv_file(): void
        write data to csv file
    """
    
    def __init__(self):
        self.accounts = []
        self.total_row = 0
        
    
    def read_data_from_csv_file(self, file_name):
        """
            read data from csv file
            
            arguments:
                file_name: path and name of csv file to read
        """
        try:
            print ("Begin read csv file")
            with open(file_name, "r") as file:
                reader = csv.reader(file, delimiter = ",")
                for index, row_data in enumerate(reader):
                    if index == 0:
                        continue
                    else:
                        user_info = {
                            "id":row_data[ID_INDEX],
                            "username":row_data[USERNAME_INDEX],
                            "password":row_data[PWD_INDEX],
                            "full_name":row_data[FULL_NAME_INDEX]
                            }
                
                        self.accounts.append(Account(user_info))
                        self.total_row +=1
            print("read data from csv file successfully")
        except IOError as file_err:
            print ("read data from csv file fail")
#             print (file_err)
            raise
        except FileNotFoundError as file_err:
            print ("read data from csv file fail")
#             print (file_err)
            raise
    
    
    def get_list_data(self, is_encoding=False, is_filter_full_name=False):
        """
            get list of data read from csv file
            
            Arguments:
                is_encoding: encoding password or not
                is_filter_full_name: filter with full name not null or not
        """
        
        data_filter = filter(lambda x: x.full_name != "", self.accounts) if is_filter_full_name else self.accounts
        
            
        return json.dumps({
            "total_row":self.total_row,
            "new_accounts":[{
                "id": account.id,
                "username": account.username,
                "password": account.encode_pwd() if is_encoding else account.password,
                "full_name": account.full_name,
            } for account in data_filter
        ]})
            
        
    
    
        
        
    def get_full_name_with_prefix(self, pre_value=""):
        """
            get list data with full name start with a
        """
        data = filter(lambda x: x.full_name.startswith(pre_value), self.accounts)
#         data = filter(lambda x: pre_value in x.full_name  , self.accounts)
        return json.dumps({
                "total_row":self.total_row,
                "new_accounts":[{
                    "id": account.id,
                    "username": account.username,
                    "password": account.encode_pwd(),
                    "full_name": account.full_name,
                } for account in data
            ]})
        
    
        
    def write_data_to_csv_file(self):
        """    
            write data to csv file
        """
        data = filter(lambda x: x.full_name != "", self.accounts)
        try:
            print("begin write data to csv file")
            with open("data_new.csv", mode="w") as csv_file:
                writer = csv.writer(csv_file, delimiter = ",")
                writer.writerow(["id","user_name","password","full_name"])
                
                for account in data:
                    writer.writerow([account.id, account.username, 
                                     account.encode_pwd(), 
                                     account.full_name])
                    
            print ("write data to csv file successfully")
        except EOFError as err:
            print ("write data to csv file fail")

   
    
if __name__ == "__main__":
    ra = RegisterAccount()
    #read data from csv file
    ra.read_data_from_csv_file("MOCK_DATA.csv")
    #get list of data read from csv file
    print(ra.get_list_data(is_encoding=False, is_filter_full_name = False))
    #get list data with encode pwd with base 64
    print(ra.get_list_data(is_encoding=True, is_filter_full_name = False))
    #get list data with full name not null
    print(ra.get_list_data(is_encoding=True, is_filter_full_name = True))
    #write data to csv file successfully
    ra.write_data_to_csv_file()
    print(ra.get_full_name_with_prefix(pre_value='A'))
    
    