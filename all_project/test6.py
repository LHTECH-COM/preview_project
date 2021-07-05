import requests
import json


API_URL = "https://jsonplaceholder.typicode.com/users"

USERNAME_TYPE = 1
NAME_TYPE = 2
COMPANY_TYPE = 3

class Users(object):
    """
    A class to store information of user
    
    Attributes:
    -------------------
    user_list: array of string
        list of information of user
            
    Methods:
    ---------------------
    get_data_from_api(): object
        return list of user data from api
    """
    
    def __init__(self):
        """
        user data get from api
        """
        self.user_list = []
        
    def get_data_from_api(self):
        """    
        get data from api
        
        Returns
        ----------------
        list
            list of user get from api
        """
        try:
            response = requests.get(API_URL)
            if response.status_code == 200:
                response_data = response.json()
                self.user_list = list(data for data in response_data)
            else:
                response.raise_for_status()
        except requests.exceptions.HTTPError as htt_err:
            print(htt_err)
        except requests.exceptions.ConnectionError as htt_err:
            print(htt_err)
        except requests.exceptions.Timeout as htt_err:
            print(htt_err)
        except requests.exceptions.RequestException as htt_err:
            print(htt_err)
            
    def search_by_value(self, search_value, search_type):
        """
        search data by search value and search type
        
        arguments:
        ----------------------
        search_value: str
            value to search
        search_type: int
            type of search
            
        Returns:
        -------------------
        list
            list of user
        """
        data_filter = []
        try:
            if search_type == COMPANY_TYPE:
                data_filter = list(data for data in self.user_list if data["company"]["name"] == search_value)
            elif search_type == USERNAME_TYPE:
                data_filter = list(data for data in self.user_list if data["username"] == search_value)
            elif search_type == NAME_TYPE:
                data_filter = list(data for data in self.user_list if data["name"].startswith(search_value))
            
        except KeyError as err:
            pass
        
        return data_filter
    
    def search_by_company_name(self, search_value = ""):
        """
        search data by company name
        
        arguments:
        ---------------------
        search_value: str
            value want to search
            
        Returns:
        --------------------------
        list
            list of user search by company name
        """
        data_filter = self.search_by_value(search_value, COMPANY_TYPE)
        print (data_filter) if data_filter else print("data not found")
        
    def search_by_name(self, search_value = ""):
        """
        search data by name
        
        arguments:
        -----------------------
        search_value: str
            value want to search
            
        Returns:
        --------------------------
        list
            list of user search by company name
        """
        data_filter = self.search_by_value(search_value, NAME_TYPE)
        print (data_filter) if data_filter else print("data not found")
        
    def search_by_username(self, search_value = ""):
        """
        search data by user name
        
        arguments:
        -----------------
        search_value: str
            value want to search
            
        Returns:
        --------------------------
        list
            list of user search by company name
        """
        data_filter = self.search_by_value(search_value, USERNAME_TYPE)
        print (data_filter) if data_filter else print("data not found")
        
if __name__ == "__main__":
    user = Users()
    user.get_data_from_api()
    print ("search by company:")
    user.search_by_company_name("Yost and Sons")
    print ("search by name start with C")
    user.search_by_name(search_value = "C")
    print("search by username")
    user.search_by_username("Moriah.Stanton")
        
        
        
        
        
        