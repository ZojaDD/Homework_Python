import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.maximize_window() # Максимизируем окно браузера
    driver.set_page_load_timeout(10) # Ожидание загрузки страницы
    yield driver
    driver.quit() # Закрыть браузер после завершения тестов

def test_calculator(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    
    # В поле ввода по локатору #delay введите значение 45.
    element = driver.find_element(By.CSS_SELECTOR, "#delay")
    element.clear()
    element.send_keys("45")

    #Нажмите на кнопки: "7", "+", "8", "="
    buttons = ["7", "+", "8", "="]
    for button in buttons:
        xpath = f"//span[text()='{button}']"
        driver.find_element(By.XPATH, xpath).click()
    
    #Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
    result = WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
    assert result