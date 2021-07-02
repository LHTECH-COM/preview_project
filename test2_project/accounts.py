import json
import requests

COMPANY_NAME_TYPE = 1
USER_NAME_TYPE = 2
NAME_TYPE = 3

API_URL = "https://jsonplaceholder.typicode.com/users"
class Accounts(object):
    """
        A class is information of account
        
        Attributes
        --------------------------------
        accounts: array of string return from API
        
    """
    
    def __init__(self):
        self.accounts = []
               
    
    def search_data(self, search_value="", search_type = ""):
        """
            search data from rest api
            
            Arguments:
                search_value: value want to search
                search_type: type of search: company, name, username
        """
        
        data_list = []
        try:
            response = requests.get(API_URL)
            if response.status_code == 200:
                response_data = response.json()
                for data in response_data:
                    try:
                        if search_type == COMPANY_NAME_TYPE: #search by company name
                            if data["company"]["name"] == search_value:
                                data_list.append(data)
                                continue
                        if search_type == USER_NAME_TYPE:
                            if data["username"] == search_value:
                                data_list.append(data)
                                continue
                        if search_type == NAME_TYPE:
                            if data["name"] == search_value:
                                data_list.append(data)
                                continue
                    except KeyError as key_rr:
                        pass
               
                return data_list
                
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
            
    def search_by_company(self, search_value):
        """
            search by company
            arguments:
                search_value: value want to search
        """
        data = self.search_data(search_value, COMPANY_NAME_TYPE)
        if data:
            print(data)
        else:
            print ("not found data")
            
    def search_by_username(self, search_value):
        """
            search by user name
            arguments:
                search_value: value want to search
        """
        data = self.search_data(search_value, USER_NAME_TYPE)
        if data:
            print(data)
        else:
            print ("not found data")
            
    def search_by_name(self, search_value):
        """
            search by name
            arguments:
                search_value: value want to search
        """
        data = self.search_data(search_value, NAME_TYPE)
        
        if data:
            print(data)
        else:
            print ("not found data")
        
ac = Accounts()

ac.search_by_company(search_value = "Romaguera-Crona")
ac.search_by_name(search_value = "Ervin Howell")
ac.search_by_username(search_value = "Karianne")


