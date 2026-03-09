from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CardPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def fill_form(self):
        self.driver.find_element(
            By.ID, "first-name").send_keys("Зоя")
        self.driver.find_element(
            By.ID, "last-name").send_keys("Иванова")
        self.driver.find_element(
            By.ID, "postal-code").send_keys("333222")

    def click_continue(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "continue"))).click()
