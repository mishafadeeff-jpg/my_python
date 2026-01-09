from dataclasses import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage


@dataclass
class InventoryPage(BasePage):
    driver: WebDriver

    BACKPACK_ADD = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT_ADD = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self) -> "InventoryPage":
        self.click(self.BACKPACK_ADD)
        return self

    def add_bolt_tshirt(self) -> "InventoryPage":
        self.click(self.BOLT_TSHIRT_ADD)
        return self

    def add_onesie(self) -> "InventoryPage":
        self.click(self.ONESIE_ADD)
        return self

    def open_cart(self) -> None:
        self.click(self.CART_LINK)
