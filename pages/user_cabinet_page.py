import allure
from pages.base_page import BasePage
from locators.user_cabinet_locators import UserCabinetLocators
from locators.base_locators import BaseLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from urls import USER_ORDER_HISTORY, USER_CABINET_LOGIN


class UserCabinetPage(BasePage):

    @allure.step("Кликнуть по кнопке 'Личный кабинет' в хедере")
    def click_header_cabinet_button(self):
        self.js_click(BaseLocators.HEADER_CABINET_BUTTON)

    @allure.step("Перейти в раздел 'История заказов'")
    def click_orders_history_button(self):
        self.click(UserCabinetLocators.ORDERS_HISTORY_BUTTON)

    @allure.step("Получить список номеров заказов из истории пользователя")
    def get_history_order_numbers(self):
        elements = self.get_elements_with_retry_on_refresh(
            locator=UserCabinetLocators.ORDERS_HISTORY_NUMBERS,
            url_trigger_text=USER_ORDER_HISTORY
        )        
        return [el.text.strip().lstrip('#').lstrip('0') for el in elements]   

    @allure.step("Кликнуть по кнопке выхода из аккаунта")
    def click_exit_button(self):
        self.click(UserCabinetLocators.USER_EXIT_BUTTON)

    @allure.step("Ожидать загрузку страницы авторизации после выхода")
    def wait_for_login_page_load(self):
        return self.wait_for_url(USER_CABINET_LOGIN)
