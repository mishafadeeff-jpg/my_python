from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)

third_image = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "award"))
)

third_image_src = third_image.get_attribute("src")
print(third_image_src)

driver.quit()
