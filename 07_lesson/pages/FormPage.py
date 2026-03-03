from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

red_color = "rgba(248, 215, 218, 1)"
green_color = "rgba(15, 81, 50, 1)"

class FormPage:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 5)
    
    def open(self):
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[type="submit"]'))
        )

    def fill_form(self):
        self._driver.find_element(By.NAME, "first-name").send_keys("Иван")
        self._driver.find_element(By.NAME, "last-name").send_keys("Петров")
        self._driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        self._driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        self._driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        self._driver.find_element(By.NAME, "city").send_keys("Москва")
        self._driver.find_element(By.NAME, "country").send_keys("Россия")
        self._driver.find_element(By.NAME, "job-position").send_keys("QA")
        self._driver.find_element(By.NAME, "company").send_keys("SkyPro")
    
    def submit_form(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[type="submit"]'))
        )
        submit_button_element = self._driver.find_element(
            By.XPATH, "//button[@type='submit']"
            )
        self._driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            submit_button_element
            )
        wait = WebDriverWait(self._driver, 10)
        submit_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit']"))
        )
        self._driver.find_element(
            By.XPATH, "//button[@type='submit']").click()
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "container"))
                )
    
    def check_zip_code_error(self):
        zip_field = self._driver.find_element(
            By.CSS_SELECTOR, "#zip-code"
            )
        actual_zip_color = zip_field.value_of_css_property(
            "background-color"
            )

        assert actual_zip_color == red_color, \
            f"Поле Zip code должно быть красным. Ожидался: \
                {red_color}, получен: {actual_zip_color}"
        
    def check_fields_success(self):
        green_fields_ids = [
            "#first-name", "#last-name", "#address", "#e-mail", "#phone",
            "#city", "#country", "#job-position", "#company"
        ]
        for field_id in green_fields_ids:
            element = self._driver.find_element(
                By.CSS_SELECTOR, field_id
                )
            actual_color = element.value_of_css_property("color")
            assert actual_color == green_color, \
                f"Поле '{field_id}' должно быть зеленым."\
                f"Ожидался: {green_color}, получен: {actual_color}"
    