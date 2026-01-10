import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    service = FirefoxService(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    d = webdriver.Firefox(service=service, options=options)
    d.maximize_window()
    yield d
    d.quit()


def test_total_is_58_29(driver):
    login_page = LoginPage(driver)
    login_page.open().login_as("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_backpack().add_bolt_tshirt().add_onesie().open_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_customer_info("Misha", "Faddeev", "610000")
    total = checkout.read_total()

    assert total == 58.29

    driver.quit()
