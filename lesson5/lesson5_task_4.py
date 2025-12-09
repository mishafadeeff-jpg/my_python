from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
import time

service = FirefoxService(
    r"C:\Users\misha\OneDrive\Desktop\Домашка\
    Test\my_python\lesson5\geckodriver.exe"
)

driver = webdriver.Firefox(service=service)

try:

    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(2)

    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("tomsmith")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()

    time.sleep(2)

    message = driver.find_element(By.ID, "flash").text

    print(message)
finally:
    driver.quit()
