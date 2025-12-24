from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
import time


service = FirefoxService(
    r"C:\Users\misha\OneDrive\Desktop\Домашка"
    r"\Test\my_python\lesson5\geckodriver.exe"
)

driver = webdriver.Firefox(service=service)

try:

    driver.get("http://the-internet.herokuapp.com/inputs")
    time.sleep(2)

    input_field = driver.find_element(By.TAG_NAME, "input")

    input_field.send_keys("Sky")
    time.sleep(2)

    input_field.clear()
    time.sleep(1)

    input_field.send_keys("Pro")

    time.sleep(3)
finally:

    driver.quit()
