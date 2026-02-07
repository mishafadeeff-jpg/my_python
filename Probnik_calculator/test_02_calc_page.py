import pytest
from selenium import webdriver
from pages.СаclMainPage import CalcMainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "num1, operation, num2, expected_result, delay",
    [
        ("7", "+", "8", "15", 15),
        ("9", "-", "3", "6", 10),
        ("4", "x", "5", "20", 20),
        ("8", "÷", "2", "4", 5),
    ],
)
def test_calculator_flow(driver, num1, operation,
                         num2, expected_result, delay):
    main_page = CalcMainPage(driver)

    main_page.open()
    main_page.set_delay(delay)
    main_page.click_buttons([num1, operation, num2, "="])
    main_page.wait_for_result(expected_result, delay)

    assert main_page.get_result() == expected_result, \
        f"Expected result:{expected_result}, but got:{main_page.get_result()}"
