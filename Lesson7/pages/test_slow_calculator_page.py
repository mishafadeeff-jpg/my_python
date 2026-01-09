import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from slow_calculator_page import SlowCalculatorPage  # ВАЖНО: без pages.


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    d = webdriver.Chrome(service=service, options=options)
    d.maximize_window()
    yield d
    d.quit()


def test_result_is_15(driver):
    page = SlowCalculatorPage(driver)

    page.open() \
        .set_delay(45) \
        .press_sequence("7+8=")

    page.wait_screen_contains("15", timeout_seconds=55)

    # Проверка только в тесте — как требуется
    assert page.get_screen_text() == "15"
