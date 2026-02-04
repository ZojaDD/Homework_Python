from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# Перейти на страницу
driver.get("http://uitestingplayground.com/classattr")

# Кликнуть на синюю кнопку
driver.find_element(By.CLASS_NAME, "btn-primary").click()

sleep(5)
