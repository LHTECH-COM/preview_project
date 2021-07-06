import csv
import json


class Users(object):
    """
    A class used to represent an user
    
    Methods:
    ------------------
    get_full_name(): str
        return full name of user
    """
    
    def __init__(self, id, first_name, last_name, email, gender, state):
        """
        parameters:
        ----------------
        id: int
            id of user
        first_name: str
            first name of user
        last_name: str
            last name of user
        email: str
            email of user
        gender: str
            gender of user
        state: str
            state of user
        """
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.state = state
        
        
    def get_full_name(self):
        """
        get full name of user
        
        Returns:
        ------------------------
        str
            full name of user
        """
        return f'{self.first_name} {self.last_name}'
        
class RegisterUser(object):
    """
    A class to store data read from csv file
    
    Attributes:
    ----------------------------
    user_lists_data: array of string
            list of user read from csv file
            
    Methods:
    ---------------------
    read_data_from_csv_file(file_name):
        read data from csv file
    merge_data():
        merge data from 2 csv file
    write_data_to_csv_file():
        write data to csv file
    """
    
    def __init__(self):
        """
        array list of user
        """
        self.user_lists_data = []
        
        
    
    def read_data_from_csv_file(self, file_name):
        """
        read data from csv file
        parameters:
        ---------------------------
        file_name: str
            the file location of csv file
        
        Returns:
        -------------------------
        list:
            list of user read from csv file
        """
        try:
            with open(file_name, "r") as file:
#                 reader = csv.reader(file, delimiter=",")
                reader = csv.DictReader(file)
                for re in reader:
                    try:
                        id = re["id"]
                    except KeyError as err:
                        id = ""
                        
                    try:
                        first_name = re["first_name"]
                    except KeyError as err:
                        first_name = ""
                    
                    try:
                        last_name = re["last_name"]
                    except KeyError as err:
                        last_name = ""
                        
                    try:
                        email = re["email"]
                    except KeyError as err:
                        email = ""
                        
                    try:
                        gender = re["gender"]
                    except KeyError as err:
                        gender = ""
                        
                    try:
                        state = re["state"]
                    except KeyError as err:
                        state = ""
                        
                    
                    self.user_lists_data.append(Users(id, first_name, last_name, email, gender, state))
            return self.user_lists_data
                        
            print("read data from csv file successfully")
                
        except IOError as err:
            print("read data from csv file fail")



    
    def merge_data(self, file_1, file_2):
        """
        merge data from 2 csv file
        
        Parameters:
        --------------------
        file1: str
            the file location of file 1
        file2: str
            the file location of file 2
        
        Returns:
        ----------------
        list:
            list of user
        """
        self.user_lists_data = self.read_data_from_csv_file(file_1)
        data_list2 = self.read_data_from_csv_file(file_2)
        
        for da1 in self.user_lists_data:
            for da2 in data_list2:
                if da1.id == da2.id:
                    da1.state = da2.state
        
        return [json.dumps({
            "id": user.id,
            "first_name": user.first_name,
            "last_name":user.last_name,
            "full_name": user.get_full_name(),
            "email": user.email,
            "gender": user.gender,
            "state": user.state,
            }) for user in self.user_lists_data]

    def write_data_to_csv_file(self):
        """
        write data to csv file
        """
        try:
            with open("data_merge7.csv", mode="w") as csv_file:
                fieldnames = ['id', 'full_name','email','gender','state']
                writer = csv.writer(csv_file, delimiter = ",")
            
                writer.writerow(fieldnames)
                for da in self.user_lists_data:
                    writer.writerow([da.id, da.get_full_name(), da.email, da.gender, da.state])
                
            print("write data to csv file successfully")
        except EOFError as err:
            print("write data to csv file fail")
        
        
if __name__ == "__main__":
    re = RegisterUser()
    print(re.merge_data("data71.csv","data72.csv"))
    re.write_data_to_csv_file()
    
    
    
    
    
    
    
    
    
        
        
        
        