import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.slow_calculator_page import SlowCalculatorPage


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.story("Вычисления с задержкой (Slow Calculator)")
@allure.severity("normal")
@allure.title("Проверка сложения 7 + 8 = 15")
@allure.description("Тест устанавливает задержку 45 секунд,"
                    " вводит пример и ждет верный результат.")
def test_result_is_15(driver):
    # Инициализация страницы
    page = SlowCalculatorPage(driver)

    with allure.step("1. Подготовка: открытие и установка задержки"):
        page.open()
        page.set_delay(45)

    with allure.step("2. Выполнение вычислений"):
        page.press_sequence("7+8=")

    with allure.step("3. Ожидание результата"):
        page.wait_screen_contains(expected="15", timeout_seconds=55)

    with allure.step("4. Проверка"):
        result = page.get_screen_text()
        assert result == "15", f"Ожидалось 15, но на экране {result}"
