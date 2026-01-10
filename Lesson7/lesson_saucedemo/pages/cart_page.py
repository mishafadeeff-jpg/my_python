from dataclasses import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


@dataclass
class CartPage:
    driver: WebDriver

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
