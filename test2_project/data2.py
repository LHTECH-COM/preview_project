import requests
import json

API_URL = "https://jsonplaceholder.typicode.com/users"

COMPANY_TYPE = 1
NAME_TYPE = 2
USERNAME_TYPE = 3

class Users(object):
    """
        A class is information of user
        
        
        Attributes
        -------------------------
        accounts: array of str
            list of user read from api
            
            
        Methods
        ------------------------
        search_by_value(): object
            return list of user search by name or username or company name
        search_by_name(): object
            return list of user search by name
    """
    
    def __init__(self):
        self.accounts = []
        
    def get_api_value(self):
        """
            get list of data from api
        """
        try:
            response = requests.get(API_URL)
            if response.status_code == 200:
                response_data = response.json()
                for data in response_data:
                    self.accounts.append(data)
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
        
    def search_by_value(self, search_value, search_type):
        """
            filter list of data by search type and search value
            
            Arguments:
                search_value: value want to search
                search_type: type of search
        """
        #list of array data
        data_filter = []
        for data in self.accounts:
            try:
                if search_type == COMPANY_TYPE:
                    if data["company"]["name"] == search_value:
                        data_filter.append(data)
                        continue
                if search_type == NAME_TYPE:
                    if data["name"].startswith(search_value):
                        data_filter.append(data)
                        continue
                if search_type == USERNAME_TYPE:
                    if data["username"] == search_value:
                        data_filter.append(data)
                        continue
                
            except KeyError as key_err:
                pass
            
        return data_filter
    
    def search_by_company(self, search_value = ""):
        data_return = self.search_by_value(search_value, COMPANY_TYPE)
        if data_return:
            print (data_return)
        else:
            print ("data not found")
            
    def search_by_name(self, search_value = ""):
        data_return = self.search_by_value(search_value, NAME_TYPE)
        if data_return:
            print (data_return)
        else:
            print ("data not found")
            
    def search_by_user_name(self, search_value = ""):
        data_return = self.search_by_value(search_value, USERNAME_TYPE)
        if data_return:
            print (data_return)
        else:
            print ("data not found")
        
ac = Users()
ac.get_api_value()
print ("search by company:")
ac.search_by_company("Yost and Sons")
print ("search by name start with C")
ac.search_by_name(search_value = "C")
print("search by username")
ac.search_by_user_name("Moriah.Stanton")