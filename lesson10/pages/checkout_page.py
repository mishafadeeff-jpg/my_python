import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить данные покупателя")
    def fill_customer_info(
            self, first: str, last: str, postal: str) -> "CheckoutPage":
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.POSTAL_CODE, postal)
        self.click(self.CONTINUE_BUTTON)
        return self

    @allure.step("Считать итоговую сумму")
    def read_total(self) -> float:
        text = self.get_text(self.TOTAL_LABEL)
        # Строка выглядит так: "Total: $58.29". Берем то, что после $
        amount_str = text.split("$")[1]
        return float(amount_str)
