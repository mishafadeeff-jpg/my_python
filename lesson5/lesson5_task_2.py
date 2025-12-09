from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service(r"C:\Users\misha\OneDrive\
Desktop\Домашка\Test\my_python\lesson5\chromedriver.exe")

driver = webdriver.Chrome(service=service)

try:

    driver.get("http://uitestingplayground.com/dynamicid")
    time.sleep(3)

    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    blue_button.click()

    time.sleep(5)
finally:

    driver.quit()
