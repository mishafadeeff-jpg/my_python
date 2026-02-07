import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
    BACKPACK_ADD = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT_ADD = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавить рюкзак в корзину")
    def add_backpack(self) -> "InventoryPage":
        self.click(self.BACKPACK_ADD)
        return self

    @allure.step("Добавить футболку Bolt T-Shirt")
    def add_bolt_tshirt(self) -> "InventoryPage":
        self.click(self.BOLT_TSHIRT_ADD)
        return self

    @allure.step("Добавить комбинезон Onesie")
    def add_onesie(self) -> "InventoryPage":
        self.click(self.ONESIE_ADD)
        return self

    @allure.step("Перейти в корзину")
    def open_cart(self) -> None:
        self.click(self.CART_LINK)
