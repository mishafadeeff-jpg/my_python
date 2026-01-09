from __future__ import annotations
from dataclasses import dataclass

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@dataclass
class SlowCalculatorPage:
    driver: WebDriver
    url: str = ("https://bonigarcia.dev/selenium-webdriver"
                "-java/slow-calculator.html")

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def open(self) -> "SlowCalculatorPage":
        self.driver.get(self.url)
        return self

    def set_delay(self, seconds: int | str) -> "SlowCalculatorPage":
        el = self.driver.find_element(*self.DELAY_INPUT)
        el.clear()
        el.send_keys(str(seconds))
        return self

    def press(self, text: str) -> "SlowCalculatorPage":
        self.driver.find_element(By.XPATH,
                                 f"//span[normalize-space()='{text}']").click()
        return self

    def press_sequence(self, seq: str) -> "SlowCalculatorPage":
        for ch in seq:
            self.press(ch)
        return self

    def wait_screen_contains(self, expected: str, timeout_seconds: int) \
            -> None:
        WebDriverWait(self.driver, timeout_seconds).until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
        )

    def get_screen_text(self) -> str:
        return self.driver.find_element(*self.SCREEN).text.strip()
