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

# Отправить GET-запрос
response = requests.get(url, params=params)

# Проверить ответ
print(response.status_code)
print(response.json())