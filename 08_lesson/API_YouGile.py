from dotenv import load_dotenv
import os
import requests

# Загрузить переменные из .env
load_dotenv()
url = os.getenv('base_url')
login = os.getenv('login')
password = os.getenv('password')
company_id = os.getenv('company_id')
API_key = os.getenv('API_key')
token = "SAxeR+W3BkrLoNjuLgPSeW73lkEhgMpLmIujOIPcZGAX7KKM0djsb3LcPSnODy47"
params = {
        "login": login,
        "password": password,
        "companyId": company_id
        }

my_headers = {
    'Content-Type': 'application/json',
    'Authorization': f"Bearer {API_key}"
}

class API_YouGile:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv('base_url')
        self.login = os.getenv('login')
        self.password = os.getenv('password')

    def get_api_key(self, login=os.getenv("login"), password=os.getenv("password"),
                    company_id=os.getenv("company_id")):
        params = {
            'login': login,
            'password': password,
            'company_id': company_id
        }
        response = requests.post(self.url + '/api-v2/auth/keys', json=params)
        print(response.text)
        return response.json()['key']

    def get_list_projects(self, headers):
        response = requests.get(self.url + "/api-v2/projects", headers=my_headers)
        return response.json()

