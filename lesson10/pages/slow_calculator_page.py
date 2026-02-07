import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage(BasePage):
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        super().__init__(driver,
                         "https://bonigarcia.dev/selenium-"
                         "webdriver-java/slow-calculator.html")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> "SlowCalculatorPage":
        self.driver.get(self.url)
        return self

    @allure.step("Установить задержку {seconds} секунд")
    def set_delay(self, seconds: int) -> "SlowCalculatorPage":
        self.type(self.DELAY_INPUT, str(seconds))
        return self

    @allure.step("Нажать на кнопку '{text}'")
    def press(self, text: str) -> "SlowCalculatorPage":
        button_locator = (By.XPATH, f"//span[text()='{text}']")
        self.click(button_locator)
        return self

    @allure.step("Ввести последовательность: {seq}")
    def press_sequence(self, seq: str) -> "SlowCalculatorPage":
        for char in seq:
            self.press(char)
        return self

    @allure.step("Ожидать появление результата '{expected}'")
    def wait_screen_contains(self,
                             expected: str, timeout_seconds: int = 50) -> None:
        WebDriverWait(self.driver, timeout_seconds).until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
        )

    @allure.step("Получить текст с экрана")
    def get_screen_text(self) -> str:
        return self.get_text(self.SCREEN)
