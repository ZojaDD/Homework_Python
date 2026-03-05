from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainShopPage:
    def __init__(self, driver):
        self.driver = driver

    def shop_page(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-onesie"))).click()

    def transfer_cart(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link"))).click()
