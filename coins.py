import requests

API_URL = 'https://coinsbot202.herokuapp.com/api/'

def dict_to_query(dict):
    string = ""
    for (key, value) in dict.items():
        string = string + key + "=" + value + "&"
    string = string[:-1]
    return string

class Account:

    def __init__(self, email, token):
        if type(email) != str or type(token) != str:
            raise AssertionError("Incorrect input type")
        self.email = email
        self.token = token
        self.balance = -1
        self.request_log = []

    def __str__(self):
        message = self.email + " has balance " + str(self.balance)
        return message

    def call_api(self, endpoint, req_dict):
        if type(endpoint) != str or endpoint != "balance":          
            raise AssertionError("Endpoint not valid")
        req_dict["token"] = self.token
        request_url = API_URL + endpoint + '?' + dict_to_query(req_dict)
        result = requests.get(url=request_url).json()
        if result["status"] != "OK":
            raise AssertionError(result["message"])
        else:
            return result

    def retrieve_balance(self):
        called_dict = self.call_api("balance", {'email': self.email})
        current_balance = int(called_dict["message"])
        self.balance = current_balance
        return self.balance
