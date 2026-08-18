import allure
from pages.base_page import BasePage
from locators.homepage_locators import HomePageLocators


class HomePage(BasePage):
    
    @allure.step("Открыть главную страницу Stellar Burgers")
    def open_home_page(self):
        self.go_home()

