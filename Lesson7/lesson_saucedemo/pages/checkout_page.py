from dataclasses import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


@dataclass
class CheckoutPage:
    driver: WebDriver

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def fill_customer_info(self, first: str, last: str, postal: str)\
            -> "CheckoutPage":
        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        return self

    def read_total(self) -> float:
        text = self.driver.find_element(*self.TOTAL_LABEL).text
        amount_str = text.split("$")[1]
        return float(amount_str)

    def finish(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()
