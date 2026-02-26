from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Перейти на страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Кликнуть на синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
blue_button.click()

sleep(10)
