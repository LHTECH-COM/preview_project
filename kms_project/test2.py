import requests
import json
import datetime

API_KEY = "61bfcbf31791dbc5404450267bcc23bd"
AVAILABLE_CURR = ["EUR","USD","CAD","JPY"]


class ExchangeRate(object):
    """
    Exchange money from one currency to destination currency 
    
    Attributes
    ----------------------
    base_currency: str
        base currency
    amount: int
        amount to exchange
        
        
    Methods
    -----------------------
    exchange_rate():
        return exchange rate as json format
    exchange_rate_date():
        return exchange rate at special date as json format
    """
    
    def __init__(self, base_currency="", amount=0):
        """
        init base_currency and amount
        
        Parameters:
        ------------------
        base_currency: str
            base currency
        amount: int
            amount to exchange
        """
        self.base_currency = base_currency
        self.amount = amount
        
    def exchange_rate(self, des_currency = ""):
        """
        exchange money from one currency to destination currency
        
        Parameters:
        -----------------------------------
        des_currency: str, optional
            destination currency to exchange, if empty return 3 remain currency in AVAILABLE_CURR
        """
        if des_currency:
            try:
                api_link = f'http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&base={self.base_currency}&symbols={des_currency}'
                response = requests.get(api_link)
                if response.status_code == 200:
                    response_data = response.json()
                    return json.dumps({
                            "base_currency": self.base_currency,
                            "amount": self.amount,
                            "exchange_rate_date":response_data["date"],
                            "exchange_value":
                            {des_currency: self.amount * response_data["rates"][des_currency]}
                        })
                else:
                    response.raise_for_status()
            except requests.exceptions.HTTPError as htt_err:
                print(htt_err)
            except requests.exceptions.ConnectionError as conn_err:
                print(conn_err)
            except requests.exceptions.Timeout as tim_err:
                print(tim_err)
            except requests.exceptions.RequestException as req_err:
                print(req_err)

        else:
            try:
                other_currency = [currency for currency in AVAILABLE_CURR if currency != self.base_currency]
                api_link = f'http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&base={self.base_currency}&symbols={",".join(other_currency)}'
                response = requests.get(api_link)
                if response.status_code == 200:
                    response_data = response.json()
                    return json.dumps({
                            "base_currency": self.base_currency,
                            "amount": self.amount,
                            "exchange_rate_date":response_data["date"],
                            "exchange_value":
                            [{pick_currency: self.amount * response_data["rates"][pick_currency]
                             
                             } for pick_currency in other_currency]
                        })
                else:
                    response.raise_for_status()
            except requests.exceptions.HTTPError as htt_err:
                print(htt_err)
            except requests.exceptions.ConnectionError as conn_err:
                print(conn_err)
            except requests.exceptions.Timeout as tim_err:
                print(tim_err)
            except requests.exceptions.RequestException as req_err:
                print(req_err)
                
                
    def exchange_rate_date(self, day, des_currency = ""):
        """
        exchange money from one currency to destination currency
        
        Parameters:
        -----------------------------------
        des_currency: str
            destination currency to exchange, if empty return 3 remain currency in AVAILABLE_CURR
        day: date
            day to exchange
        """
        day = day if day else datetime.date.today.strftime("%Y-%m-%d")
        if des_currency:
            try:
                api_link = f'http://api.exchangeratesapi.io/v1/{day}?access_key={API_KEY}&base={self.base_currency}&symbols={des_currency}'
                response = requests.get(api_link)
                if response.status_code == 200:
                    response_data = response.json()
                    return json.dumps({
                            "base_currency": self.base_currency,
                            "amount": self.amount,
                            "exchange_rate_date":response_data["date"],
                            "exchange_value":
                            {des_currency: self.amount * response_data["rates"][des_currency]}
                        })
                else:
                    response.raise_for_status()
            except requests.exceptions.HTTPError as htt_err:
                print(htt_err)
            except requests.exceptions.ConnectionError as conn_err:
                print(conn_err)
            except requests.exceptions.Timeout as tim_err:
                print(tim_err)
            except requests.exceptions.RequestException as req_err:
                print(req_err)

        else:
            try:
                other_currency = [currency for currency in AVAILABLE_CURR if currency != self.base_currency]
                api_link = f'http://api.exchangeratesapi.io/v1/{day}?access_key={API_KEY}&base={self.base_currency}&symbols={",".join(other_currency)}'
                response = requests.get(api_link)
                if response.status_code == 200:
                    response_data = response.json()
                    return json.dumps({
                            "base_currency": self.base_currency,
                            "amount": self.amount,
                            "exchange_rate_date":response_data["date"],
                            "exchange_value":
                            [{pick_currency: self.amount * response_data["rates"][pick_currency]
                             
                             } for pick_currency in other_currency]
                        })
                else:
                    response.raise_for_status()
            except requests.exceptions.HTTPError as htt_err:
                print(htt_err)
            except requests.exceptions.ConnectionError as conn_err:
                print(conn_err)
            except requests.exceptions.Timeout as tim_err:
                print(tim_err)
            except requests.exceptions.RequestException as req_err:
                print(req_err)



if __name__ == "__main__":
    ex = ExchangeRate(base_currency="EUR", amount=2)
    print("exchange to USD")
    print(ex.exchange_rate("USD"))
    print("exchange to empty destination currency")
    print(ex.exchange_rate())
    print("exchange 2021-06-28 to USD")
    print(ex.exchange_rate_date("2021-06-28", "USD"))
    print("exchange 2021-06-28 to empty destination currency")
    print(ex.exchange_rate_date("2021-06-28"))




