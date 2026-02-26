import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window() # Максимизируем окно браузера
    driver.set_page_load_timeout(10) # Ожидание загрузки страницы
    yield driver
    driver.quit() # Закрыть браузер после завершения тестов

def test_shopping_cart_total(driver):    
    #Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
    driver.get("https://www.saucedemo.com/")

    # Авторизуйтесь как пользователь "standard_user", пароль: "secret_sauce"
    username = "#user-name"
    username_input = driver.find_element(By.CSS_SELECTOR, username)
    username_input.send_keys("standard_user")

    password = "#password"
    password_input = driver.find_element(By.CSS_SELECTOR, password)
    password_input.send_keys("secret_sauce")

    # Нажать кнопку Login
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    # Добавьте в корзину товары: Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie.

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))).click()


    # Перейдите в корзину.
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

    # Нажмите Checkout.
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # Заполните форму своими данными:имя, фамилия, почтовый индекс.
    first_name = driver.find_element(By.ID, "first-name").send_keys("Зоя")
    last_name = driver.find_element(By.ID, "last-name").send_keys("Иванова")
    address = driver.find_element(By.ID, "postal-code").send_keys("333222")
        
    # Нажмите кнопку Continue.
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "continue"))).click()

    # Прочитайте со страницы итоговую стоимость (Total)
    text_prise = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    text_prise_value = float(text_prise.split("$")[1])

    # Проверьте, что итоговая сумма равна $58.29
    assert text_prise_value == 58.29