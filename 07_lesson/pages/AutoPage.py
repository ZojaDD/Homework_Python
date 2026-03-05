from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class AutoPage:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self._driver.get("https://www.saucedemo.com/")

    # Авторизуйтесь как пользователь "standard_user",
    # пароль: "secret_sauce"
    def authorization(self):
        username = "#user-name"
        username_input = self._driver.find_element(By.CSS_SELECTOR, username)
        username_input.send_keys("standard_user")
        password = "#password"
        password_input = self._driver.find_element(By.CSS_SELECTOR, password)
        password_input.send_keys("secret_sauce")
        self._driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()  # Нажать кнопку Login
