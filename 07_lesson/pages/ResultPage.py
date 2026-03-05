from selenium.webdriver.common.by import By


class ResultPage:
    def __init__(self, driver):
        self.driver = driver

    def summary(self):
        text_prise = self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
        text_prise_value = float(text_prise.split("$")[1])
        return text_prise_value
