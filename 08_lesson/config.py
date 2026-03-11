from dotenv import load_dotenv
import os
import requests


class APIconfig:
    def __init__(self, base_url):
        self.url = base_url

    def test_create_project():
        # Загрузить переменные из .env
        load_dotenv()        
        url = os.getenv('base_url')
        API_key = os.getenv('API_key')
        body = {
                "login": "drobiazkoz@yandex.ru",
                "password": "Qq-2266553",
                "companyId": "f0fde861-acc8-479e-9a00-b0ddbc0a6502"
                }


        headers = {
            "Authorization": f"Bearer {API_key}"
        }
        resp = requests.post(f"{url}/projects", json=body, headers=headers)

        print(resp.json())