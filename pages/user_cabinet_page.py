import allure
from pages.base_page import BasePage
from locators.user_cabinet_locators import UserCabinetLocators
from locators.base_locators import BaseLocators
from selenium.webdriver.common.by import By


class UserCabinetPage(BasePage):

    @allure.step("Кликнуть по кнопке 'Личный кабинет' в хедере")
    def click_header_cabinet_button(self):
        self.js_click(BaseLocators.HEADER_CABINET_BUTTON)

    @allure.step("Перейти в раздел 'История заказов'")
    def click_orders_history_button(self):
        self.click(UserCabinetLocators.ORDERS_HISTORY_BUTTON)

    @allure.step("Кликнуть по кнопке выхода из аккаунта")
    def click_exit_button(self):
        self.click(UserCabinetLocators.USER_EXIT_BUTTON)

    @allure.step("Ожидать загрузку страницы авторизации после выхода")
    def wait_for_login_page_load(self):
        from urls import USER_CABINET_LOGIN
        return self.wait_for_url(USER_CABINET_LOGIN)
