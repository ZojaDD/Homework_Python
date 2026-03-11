from dotenv import load_dotenv
import os
import requests


# Загрузить переменные из .env
load_dotenv()

# Получить значения переменных
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
company_id = os.getenv('COMPANY_ID')


# Указать URL и параметры запроса
base_url = "http://localhost:8001/api-v2/"
params = {
    'login': login,
    'password': password,
    'companyID': company_id
}

# Отправить GET-запрос
response = requests.get(base_url + 'auth/keys', params=params)

# Проверить ответ
print(response.status_code)
print(response.json())