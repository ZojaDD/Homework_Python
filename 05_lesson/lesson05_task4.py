from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By



#Открыть браузер FireFox.
driver = webdriver.Firefox()

# Перейти на страницу
driver.get("http://the-internet.herokuapp.com/login")

# В поле username ввести значение tomsmith
username = "#username"
username_input = driver.find_element(By.CSS_SELECTOR, username)
username_input.send_keys("tomsmith")

# В поле password ввести значение SuperSecretPassword!.
password = "#password"
password_input = driver.find_element(By.CSS_SELECTOR, password)
password_input.send_keys("SuperSecretPassword!")

# Нажать кнопку Login
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

sleep(5)

# Вывести текст с зеленой плашки в консоль
text_from_die = "#flash"
text = driver.find_element(By.CSS_SELECTOR, text_from_die).text
print(text)

# Закрыть браузер (метод quit()
driver.quit()




# Возвращает отображаемый текст указанного элемента
# text = driver.find_element(By.TAG_NAME, "h1").text

# print(text)