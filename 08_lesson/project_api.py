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

def test_simple_req():
    response = requests.get(url + "/projects", params=params)
    assert response.status_code == 200
    print(response.status_code)

# Получить список проектов
# Добавить проект
# Получить список проектов, проверить что добавился новый

# Авторизация
# Создать проект
# Изменить проект
# Получить по ID