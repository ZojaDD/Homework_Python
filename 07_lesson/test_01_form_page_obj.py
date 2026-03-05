import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.FormPage import FormPage


@pytest.fixture
def driver():
    edgeService = Service(
        r"C:\Users\MI\OneDrive\Desktop\first_repo\msedgedriver.exe")
    driver = webdriver.Edge(service=edgeService)
    driver.set_page_load_timeout(10)  # Ожидание загрузки страницы
    driver.maximize_window()  # Максимизируем окно браузера
    yield driver
    driver.quit()  # Закрыть браузер после завершения тестов

def test_form_submission_flow(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form()
    form_page.submit_form()
    form_page.check_zip_code_error()
    form_page.check_fields_success()

    print("Все проверки цвета пройдены успешно!")
