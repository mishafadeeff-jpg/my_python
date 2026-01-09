from dataclasses import dataclass
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@dataclass
class BasePage:
    driver: WebDriver

    def find(self, locator: tuple, timeout: int = 5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator: tuple, timeout: int = 5) -> None:
        self.find(locator, timeout).click()

    def type(self, locator: tuple, text: str, timeout: int = 5) -> None:
        el = self.find(locator, timeout)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator: tuple, timeout: int = 5) -> str:
        return self.find(locator, timeout).text
