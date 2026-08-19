from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
from urls import BASE_URL


class PasswordRecoveryPage(BasePage):
    def open_reset_page(self):
        # Открываем страницу восстановления пароля
        self.driver.get(f"{BASE_URL}/forgot-password")
        
        # Вводим тестовый email
        self.send_keys(PasswordRecoveryLocators.EMAIL_INPUT, "test_me@yandex.ru")
        
        # Кликаем по кнопке "Восстановить"
        self.js_click(PasswordRecoveryLocators.RESTORE_BUTTON)
        
        # Ждем, чтобы бэкенд обработал запрос, а браузер перешел на /reset-password
        self.wait_for_url("/reset-password")

    def click_show_password_button(self):
        self.js_click(PasswordRecoveryLocators.SHOW_PASSWORD_INPUT_BUTTON)

    def get_password_input_type(self):
        element = self.wait_visible(PasswordRecoveryLocators.PASSWORD_INPUT)
        return element.get_attribute("type")

    def get_password_container_classes(self):
        input_element = self.wait_visible(PasswordRecoveryLocators.PASSWORD_INPUT)
        
        # Поднимаемся к родительскому контейнеру <div>
        from selenium.webdriver.common.by import By
        container_element = input_element.find_element(By.XPATH, "./parent::div")
        
        # Возвращаем классы именно контейнера, где и появляется 'input_status_active'
        return container_element.get_attribute("class")