from dotenv import load_dotenv
import os
import requests

# Загрузить переменные из .env
load_dotenv()

# Получить значения переменных
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
company_id = os.getenv('COMPANY_ID')
url = os.getenv('base_url')

# Указать URL и параметры запроса
url = "https://ru.yougile.com/api-v2"
params = {
    'login': login,
    'password': password,
    'companyID': company_id
}

def list_projects():
    response = requests.get(url + "/projects/list", params=params)
    response_body = response.json()
    first_company = response_body[0]
    assert first_company["name"] == "Пример проекта"
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    print(response.status_code)
