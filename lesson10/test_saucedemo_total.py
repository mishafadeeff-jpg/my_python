import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Покупка товаров")
@allure.story("Проверка итоговой суммы заказа")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Успешная покупка товаров на сумму $58.29")
def test_total_is_58_29(driver):
    with allure.step("Авторизация"):
        login_page = LoginPage(driver)
        login_page.open().login_as("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        inventory = InventoryPage(driver, driver.current_url)
        inventory.add_backpack().add_bolt_tshirt().add_onesie().open_cart()

    with allure.step("Переход к оформлению"):
        cart = CartPage(driver, driver.current_url)
        cart.click_checkout()

    with allure.step("Ввод данных покупателя"):
        checkout = CheckoutPage(driver, driver.current_url)
        checkout.fill_customer_info("Misha", "Faddeev", "610000")

    with allure.step("Проверка итоговой суммы"):
        total = checkout.read_total()
        assert total == 58.29, (f"Сумма не совпадает. "
                                f"Ожидалось 58.29, получено {total}")
