from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Перейти на страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Ввести в поле текст Sky
input_field = driver.find_element(By.CSS_SELECTOR, "input")
input_field.send_keys("200")

sleep(5)

# очистить поле
input_field.clear()

# Ввести в поле текст Pro
input_field.send_keys("1000")

sleep(5)

# Закрыть браузер
driver.quit()
