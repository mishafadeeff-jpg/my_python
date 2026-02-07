import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver, "https://www.saucedemo.com/")

    @allure.step("Авторизация пользователя {username}")
    def login_as(self, username: str, password: str) -> "LoginPage":
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        return self
