import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver, url: str = ""):
        self.driver = driver
        self.url = url

    @allure.step("Открыть страницу")
    def open(self):
        self.driver.get(self.url)
        return self

    def find(self, locator: tuple, timeout: int = 15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator: tuple):
        self.find(locator).click()

    def type(self, locator: tuple, text: str):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple):
        return self.find(locator).text
