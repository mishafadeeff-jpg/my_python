import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self) -> None:
        self.click(self.CHECKOUT_BUTTON)
