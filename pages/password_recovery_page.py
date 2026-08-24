from pages.base_page import BasePage
from locators.base_locators import BaseLocators
from locators.password_recovery_locators import PasswordRecoveryLocators
from selenium.webdriver.common.by import By
from urls import BASE_URL, USER_FORGOT_PASSWORD, USER_RESET_PASSWORD


class PasswordRecoveryPage(BasePage):
    def open_reset_page(self):
        # Открываем страницу восстановления пароля
        self.navigate_to(f"{BASE_URL}{USER_FORGOT_PASSWORD}")
        
        # Вводим тестовый email
        self.send_keys(PasswordRecoveryLocators.EMAIL_INPUT, "test_me@yandex.ru")
        
        # Кликаем по кнопке "Восстановить"
        self.js_click(PasswordRecoveryLocators.RESTORE_BUTTON)
        
        # Ждем, чтобы бэкенд обработал запрос, а браузер перешел на /reset-password
        self.wait_for_url(USER_RESET_PASSWORD)

    def click_show_password_button(self):
        self.js_click(PasswordRecoveryLocators.SHOW_PASSWORD_INPUT_BUTTON)

    def get_password_input_type(self):
        element = self.wait_visible(PasswordRecoveryLocators.PASSWORD_INPUT)
        return element.get_attribute("type")

    def get_password_container_classes(self):
        input_element = self.wait_visible(PasswordRecoveryLocators.PASSWORD_INPUT)
        
        # Поднимаемся к родительскому контейнеру <div>
        container_element = input_element.find_element(*BaseLocators.PARENT_ELEMENT)
        
        # Возвращаем классы именно контейнера, где и появляется 'input_status_active'
        return container_element.get_attribute("class")