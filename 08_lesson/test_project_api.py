import requests

# Получить значения переменных
url = "https://ru.yougile.com"
company_id = "f0fde861-acc8-479e-9a00-b0ddbc0a6502"
login = # ваш_логин_здесь
password = # ваш_пароль
token = # ваш_токен_здесь
user_id = # ваш_user_id_здесь

# Указать URL и параметры запроса
params = {
    'login': login,
    'password': password,
    'companyId': company_id
}

my_headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Basic {token}'
}
  #Авторизация
def test_auth():
    response = requests.post(url + '/api-v2/auth/keys/get', json=params)
    response_body = response.json()
    print(response_body)
    assert response.status_code == 200

def test_add_new():
    # Получить список проектов
    response = requests.get(url + "/api-v2/projects", headers=my_headers)
    response_body = response.json()
    # Считаем количество проектов
    company_list = response_body['content']
    len_before = len(company_list)
    # Проверяем, что список проектов не пустой
    assert len(company_list) > 0
    assert response.status_code == 200
    # Добавляем новый проект
    project = {
        "title": "Домашка 8",
        "users": {
            user_id : "admin"
        }
    }
    response = requests.post(url + '/api-v2/projects', json=project, headers=my_headers)
    assert response.status_code == 201, f'пришел код ответа {response.status_code}'
    # Получить количество проектов после добавления
    response = requests.get(url + "/api-v2/projects", headers=my_headers)
    response_body = response.json()
    # Считаем количество проектов
    company_list = response_body['content']
    len_after = len(company_list)
    print(len_after)
    # Проверить, что +1
    assert len_after - len_before == 1

def test_add_negative():
    # Получить список проектов
    response = requests.get(url + "/api-v2/projects", headers=my_headers)
    response_body = response.json()
    # Считаем количество проектов
    company_list = response_body['content']
    len_before = len(company_list)
    # Пытаемся создать новый проект без названия
    project = {
        "title": "",
        "users": {
            user_id : "admin"
        }
    }
    response = requests.post(url + '/api-v2/projects', json=project, headers=my_headers)
    assert response.status_code == 400, f'пришел код ответа {response.status_code}'
    # Получить количество проектов после добавления
    response = requests.get(url + "/api-v2/projects", headers=my_headers)
    response_body = response.json()
    # Считаем количество проектов
    company_list = response_body['content']
    len_after = len(company_list)
    # Проверить, что количество проектов не изменилось
    assert len_after - len_before == 0

def test_change_project():
    # Создать новый проект
    project = {
        "title": "Новая домашка 8",
        "users": {
            user_id : "admin"
        }
    }
    response = requests.post(url + '/api-v2/projects', json=project, headers=my_headers)
    # Получить id нового проекта
    project_id = response.json().get("id")
    # Изменить название проекта
    project = {
        "title": "Изменить проект"
    }
    response = requests.put(url + f"/api-v2/projects/{project_id}", json=project, headers=my_headers)
    project_id = response.json().get("id")
    # получить измененный проект по id
    response = requests.get(url + f"/api-v2/projects/{project_id}", headers=my_headers)
    name = response.json().get("title")
    assert response.status_code == 200
    # Проверка что название изменилось
    assert name == "Изменить проект"

def test_change_negative():
    # Создать новый проект
    project = {
        "title": "Негатив",
        "users": {user_id: "admin"
        }
    }
    response = requests.post(url + '/api-v2/projects', json=project, headers=my_headers)
    # Получить id нового проекта
    project_id = response.json().get("id")
    # Изменить название проекта
    project = {
        "title": ""
    }
    response = requests.put(url + f"/api-v2/projects/{project_id}", json=project, headers=my_headers)
    project_id = response.json().get("id")
    # получить измененный проект по id
    response = requests.get(url + f"/api-v2/projects/{project_id}", headers=my_headers)
    name = response.json().get("title")
    assert response.status_code == 404, f'пришел код ответа {response.status_code}'
    # Проверка что название не изменилось
    assert name == None


def test_get_id_negative():
    # Создать новый проект
    project = {
        "title": "Негатив",
        "users": {user_id: "admin"
                  }
    }
    response = requests.post(url + '/api-v2/projects', json=project, headers=my_headers)
    # Получить id нового проекта
    project_id = response.json().get("id")
    # Попытаемся получить проект по неправильному id
    response = requests.get(url + f"/api-v2/projects/{project_id}000", headers=my_headers)
    name = response.json().get("title")
    assert response.status_code == 404, f'пришел код ответа {response.status_code}'
