import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from pages.FormPage import FormPage


@pytest.fixture
def driver():
    edgeService = Service(
        r"C:\Users\MI\OneDrive\Desktop\first_repo\msedgedriver.exe")
    driver = webdriver.Edge(service=edgeService)
    driver.set_page_load_timeout(10)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_submission_flow(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form()
    form_page.submit_form()
    form_page.check_zip_code_error()
    form_page.check_fields_success()

    print("Все проверки цвета пройдены успешно!")
