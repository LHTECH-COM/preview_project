import csv
import json


ID_INDEX = 0
FIRST_NAME_INDEX = 1
LAST_NAME_INDEX = 2
DOB_INDEX = 3

class Users(object):
    """
    A class used to represent an user
    
    Attributes:
    ----------------------
    id: int
        id of user
    first_name:
        first name of user
    last_name: str
        last name of user
    dob: str
        date of birth of user
            
    Methods:
    --------------------
    format_dob():
        format date of birth
    """
    
    def __init__(self, user_info):
        """
        parameter:
        ----------------------
        user_info: array of string
            array of string read from csv file
        """
        self.id = user_info[ID_INDEX]
        self.first_name = user_info[FIRST_NAME_INDEX]
        self.last_name = user_info[LAST_NAME_INDEX]
        self.dob = user_info[DOB_INDEX]
        
    def format_dob(self):
        """
        format date of birth
        
        returns
        ------------
        date
            date of birth format
        """
        if self.dob:
            try:
                dob = self.dob.strptime("%d%m%Y").date()
            except Exception as ex:
                dob = self.dob
        return f'{dob}'
        
class ReadUsers(object):
    """
    read data from csv file
    
    Attributes:
    ------------------
    datas: array of string
        list of user read from csv file
            
    Methods:
    ----------------------
    read_data_from_csv_file():
        read data from csv file
    get_data_list(): object
        return list of data read from csv file as json format
    id_duplicate():
        return num of row duplicate id
    get_data_no_duplicate(): object
        return list of data no duplicate id
    write_data_to_csv_file():
        write data to csv file
    """
    
    def __init__(self):
        """
        array of string read from csv file
        """
        self.datas = []
        
    def id_duplicate(self, id):
        """
        return num of row duplicate id
        arguments:
        ---------------------
        id: int
                id find duplicate
                
        Returns:
        ----------------
        int
            total num of row have duplicate id
        """
        dup_data = list(filter(lambda x: x.id == id, self.datas))
        return len(dup_data)
        
    def read_data_from_csv_file(self, file_name):
        """
        read data from csv file
        
        arguments
        -----------------------
        file_name: str
            the file location of csv file
        """
        try:
            with open(file_name, "r") as file:
                reader = csv.reader(file, delimiter=",")
                for index, row_data in enumerate(reader):
                    if index == 0:
                        continue
                    else:
                        self.datas.append(Users(row_data))
    
        except IOError as io_err:
            print("read data from csv file fail")
    
    
    def get_data_list(self):
        """
        returns
        ------------------
        list 
            a list of data read from csv file
        """
        return [json.dumps({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "dob": user.dob,
            }) for user in self.datas]
    
    def get_data_no_duplicate(self):
        """
        returns
        -----------------
        list
            a list of data with no duplicate id
        """
        data_filter = filter(lambda x: self.id_duplicate(x.id) > 1, self.datas)
        return [json.dumps({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "dob": user.dob,
            }) for user in data_filter]
        
    def write_data_to_csv_file(self):
        """
        write data to new csv file
        
        """
        try:
            with open("test4_new.csv", mode="w") as csv_file:
                writer = csv.writer(csv_file, delimiter=",")
                writer.writerow(["id","first_name","last_name","dob"])
                for data in self.datas:
                    writer.writerow([data.id, data.first_name, data.last_name, data.format_dob()])
            print("write data to csv file successfully")
        except EOFError as er:
            print("write data to csv file fail")    
    
    
if __name__ == "__main__":
    re = ReadUsers()
    re.read_data_from_csv_file("test4.csv")
    print("list of data read from csv file")
    print(re.get_data_list())
    print("list data duplicate id:")
    print(re.get_data_no_duplicate())
    re.write_data_to_csv_file()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    