from utitls import gen_n_digits
import csv 
import json
import datetime

FIRST_NAME_INDEX = 0
MIDDLE_NAME_INDEX = 1
LAST_NAME_INDEX = 2
PHONE_NUMBER_INDEX = 3
SOCIAL_ID_INDEX = 4

class Users(object):
    """
    A class is represent user
    
    Attributes
    ----------------------------
    first_name: str
        first name of user
    middle_name: str
        middle name of user
    last_name: str
        last name of user
    phone_number: int
        phone number of user
    social_id: int
        social id of user
    account_number: str
        account number of user
        
    Methods
    --------------------------
    get_full_name():
        return full name of user
    get_account_number():
        return account number of user
    
    """
    
    def __init__(self, user_info):
        """
        row data read from csv file
        """
        self.first_name = user_info[FIRST_NAME_INDEX]
        self.middle_name = user_info[MIDDLE_NAME_INDEX]
        self.last_name = user_info[LAST_NAME_INDEX]
        self.phone_number = user_info[PHONE_NUMBER_INDEX]
        self.social_id = user_info[SOCIAL_ID_INDEX]
        self.account_number = ""
        
    def get_full_name(self):
        """
        get full name of user
        """
        return f'{self.first_name } {self.middle_name} {self.last_name}'
    
    
    def get_account_number(self):
        """
        get account number of user
        """
        if not self.account_number:
            gen_8_digits = gen_n_digits(8)
            now = datetime.date.today().strftime("%m%d%y")
            self.account_number = f'IB{now}{gen_8_digits}'
        return self.account_number
    
    
class RegisterUser(object):
    """
    A class to register user read from csv file
    
    Attributes
    --------------------------------
    total_row: int    
        total of row read from csv file
    total_success: int
        total of row success: all data valid 
    total_error: int
        total of row error: some data invalid
    accounts: array of string
        list of all data reaf from csv file
        
    Methods
    ---------------------------------
    read_from_csv_file():
        read data from csv file
    check_valid_data(): bool
        return true if all data valid, fail if some of data invalid
    get_list_data():
        return list of data read from csv file as json format
    write_data_to_csv_file():
        write data to csv file
            
    """
    #phone existed 
    PHONE_LIST = []
    #list social id existed
    SOCIAL_LIST = []
    
    def __init__(self):
        """
        contains total_row, total_success, total_errors, list of user read from csv file
        """
        self.total_row = 0
        self.total_success = 0
        self.total_error = 0
        self.accounts = []
        
    def check_valid_data(self, user_info):
        """
        check all data valid or not
        
        Parameters:
        -----------------------
        user_info: array of string
            row data read from csv file
            
        Returns:
        -------------------------
        bool:
            data valid or not
            
        """
        first_name = user_info[FIRST_NAME_INDEX]
        last_name = user_info[LAST_NAME_INDEX]
        phone_number = user_info[PHONE_NUMBER_INDEX]
        social_id = user_info[SOCIAL_ID_INDEX]
        is_first_name_valid = bool(first_name.strip()) and not first_name.isnumeric()
        is_last_name_valid = bool(last_name.strip()) and not last_name.isnumeric()
        is_phone_valid = len(phone_number) == 10 and phone_number.isnumeric() and phone_number not in self.PHONE_LIST
        is_social_valid = len(social_id) == 9 and social_id.isnumeric() and social_id not in self.SOCIAL_LIST
        return is_first_name_valid and is_last_name_valid and is_phone_valid and is_social_valid
        
        
    def read_from_csv_file(self, file_name):
        """
        read data from csv file
        
        arguments:
        ---------------------
        file_name: str
            the file location of csv file
        """ 
        try:
            with open(file_name, "r") as file:
                reader = csv.reader(file, delimiter = ",")
                for index, row_data in enumerate(reader):
                    if index == 0:
                        continue
                    else:
                        if self.check_valid_data(row_data):
                            self.accounts.append(Users(row_data))
                            self.total_success +=1
                        else:
                            self.total_error +=1
                        self.total_row +=1
                        
            print("read data from csv file successfully")
        except IOError as io_err:
            print ("read data from csv file fail")
        
        
    def get_list_data(self):
        """
        list of data read from csv file
        
        Returns:
        ---------------------
        list
            list of data of user
        """
        return json.dumps({
                "total_row": self.total_row,
                "total_success": self.total_success,
                "total_error": self.total_error,
                "new_accounts":[{
                    "full_name": account.get_full_name(),
                    "phone_number": account.phone_number,
                    "social_id": account.social_id,
                    "account_number": account.get_account_number()
                    } for account in self.accounts]
            })
        
    def write_data_to_csv_file(self):
        """
        write data to csv file
        """
        try:
            print("begin write data to csv")
            with open("test1_new.csv", mode="w") as csv_file:
                writer = csv.writer(csv_file, delimiter=",")
                writer.writerow(["account_number","full_name","phone_number","social_id"])
                for data in self.accounts:
                    writer.writerow([data.get_account_number(), data.get_full_name(), data.phone_number, data.social_id])
            print("write data to csv file successfully")
        except IOError as err:
            print("write data to csv file fail")
        
if __name__ == "__main__":
    re = RegisterUser()
    print("read data from csv file")
    re.read_from_csv_file("test1.csv")
    print("list of data")
    print(re.get_list_data())
    re.write_data_to_csv_file()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        