from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open_page(self):
        self._driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')


    def delay_input_field(self):
        element = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        element.clear()
        element.send_keys("45")
    
    def press_buttons(self):
        buttons = ["7", "+", "8", "="]
        for button in buttons:
            xpath = f"//span[text()='{button}']"
            self._driver.find_element(By.XPATH, xpath).click()

    def check_result(self):
        result = WebDriverWait(self._driver, 46).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )