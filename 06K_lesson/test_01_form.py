import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

red_color = "rgba(248, 215, 218, 1)"
green_color = "rgba(15, 81, 50, 1)"


@pytest.fixture
def driver():
    edgeService = Service(
        r"C:\Users\MI\OneDrive\Desktop\first_repo\msedgedriver.exe")
    driver = webdriver.Edge(service=edgeService)
    driver.maximize_window()  # Максимизируем окно браузера
    driver.set_page_load_timeout(10)  # Ожидание загрузки страницы
    yield driver
    driver.quit()  # Закрыть браузер после завершения тестов


def test_form_submission(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[type="submit"]'))
    )

    # Заполнить поля формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[type="submit"]'))
    )

    # Получить элемент кнопки Submit
    submit_button_element = driver.find_element(By.XPATH, "//button[@type='submit']")
    # Прокрутить страницу вниз до элемента кнопки Submit
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button_element)

    # Явное ожидание, чтобы кнопка стала кликабельной
    wait = WebDriverWait(driver, 10)
    submit_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )

    # Нажимаем кнопку Submit
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Ждем, пока форма обработается
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "container")))

    zip_field = driver.find_element(By.CSS_SELECTOR, "#zip-code")
    actual_zip_color = zip_field.value_of_css_property("background-color")

    assert actual_zip_color == red_color, \
        f"Поле Zip code должно быть красным. Ожидался: {red_color}, получен: {actual_zip_color}"

    green_fields_ids = [
        "#first-name", "#last-name", "#address", "#e-mail", "#phone",
        "#city", "#country", "#job-position", "#company"
    ]

    for field_id in green_fields_ids:
        element = driver.find_element(By.CSS_SELECTOR, field_id)
        actual_color = element.value_of_css_property("color")

        assert actual_color == green_color, \
            f"Поле '{field_id}' должно быть зеленым."\
            f"Ожидался: {green_color}, получен: {actual_color}"

    print("Все проверки цвета пройдены успешно!")
