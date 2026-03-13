from dotenv import load_dotenv
import os
import requests

# Загрузить переменные из .env
load_dotenv()

# Получить значения переменных
url = os.getenv('base_url')
login = os.getenv('login')
password = os.getenv('password')
company_id = os.getenv('company_id')
API_key = os.getenv('API_key')
token = "SAxeR+W3BkrLoNjuLgPSeW73lkEhgMpLmIujOIPcZGAX7KKM0djsb3LcPSnODy47"

# Указать URL и параметры запроса
url = "https://ru.yougile.com"
params = {
    'login': login,
    'password': password,
    'companyID': company_id
}

my_headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Basic {token}'
}
  #Авторизация
def test_auth():
    response = requests.post(url + '/api-v2/auth/keys', json=params)
    print(url + '/api-v2/auth/keys')
    print(params)
    response_body = response.json()
    print(response_body)
    assert response.status_code == 200

# Получить список проектов
def test_list_projects():
    response = requests.get(url + "/api-v2/projects", headers=my_headers)
    response_body = response.json()
    print(response_body)
    first_company = response_body['content']
    print(first_company)

# Получить количество проектов
def test_list_projects():
    response = requests.get(url + "/api-v2/projects", headers=my_headers)
    response_body = response.json()
    len_before = len(response_body)
    print(response_body)
    print(len_before)

    assert len(response_body) > 0
    assert response.status_code == 200

def test_add_new():
    # Добавить проект
    response = requests.get(url + "/api-v2/projects", headers=my_headers)
    response_body = response.json()
    len_before = len(response_body)

    project = {
        "title": "Домашка 8",
        "users": {
            'b1e0e27d-d59d-483c-8c71-06681973fc95': "admin"
        }
    }
    response = requests.post(url + '/api-v2/projects', json=project, headers=my_headers)

    # Получить количество проектов после
    response_body = response.json()
    len_after = len(response_body)
    print(len_after)

    # Проверить, что +1
    assert len_after - len_before == 1


def test_change_project():
    # Создать новый проект
    project = {
        "title": "Новая домашка 8",
        "users": {
            "b1e0e27d-d59d-483c-8c71-06681973fc95": "admin"
        }
    }
    response = requests.post(url + '/api-v2/projects', json=project, headers=my_headers)
    response_body = response.json()
    # Получить id нового проекта
    project_id = response.json().get("id")
    print(project_id)

    # Изменить проект
    {
        "title": "Новый проект для домашки8"
    }
    response = requests.post(url + /api-v2/projects/{project_id}, json=project, headers=my_headers)
    response_body = response.json()



