import allure
from pages.password_recovery_page import PasswordRecoveryPage


@allure.suite("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля, кликая «Восстановить пароль»")
    def test_navigation_to_forgot_password_page(self, driver):
        recovery_page = PasswordRecoveryPage(driver)
        from urls import USER_CABINET_LOGIN, USER_FORGOT_PASSWORD, BASE_URL

        with allure.step("Открыть страницу авторизации"):
            driver.get(f"{BASE_URL}{USER_CABINET_LOGIN}")

        with allure.step("Кликнуть кнопку «Восстановить пароль»"):
            from locators.password_recovery_locators import PasswordRecoveryLocators
            recovery_page.js_click(PasswordRecoveryLocators.RECOVER_PASSWORD_BUTTON)

        with allure.step("Проверить, что произошел переход на страницу /forgot-password"):
            current_url = recovery_page.wait_and_get_url(USER_FORGOT_PASSWORD)
            assert USER_FORGOT_PASSWORD in current_url, f"Неверный URL после клика: {current_url}"

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_submit_email_for_password_recovery(self, driver):
        recovery_page = PasswordRecoveryPage(driver)
        from urls import USER_FORGOT_PASSWORD, USER_RESET_PASSWORD, BASE_URL

        with allure.step("Открыть страницу ввода почты для восстановления"):
            driver.get(f"{BASE_URL}{USER_FORGOT_PASSWORD}")

        with allure.step("Ввести почту и нажать кнопку «Восстановить»"):
            from locators.password_recovery_locators import PasswordRecoveryLocators
            recovery_page.send_keys(PasswordRecoveryLocators.EMAIL_INPUT, "test_me@yandex.ru")
            recovery_page.js_click(PasswordRecoveryLocators.RESTORE_BUTTON)

        with allure.step("Проверить редирект на страницу ввода нового пароля /reset-password"):
            current_url = recovery_page.wait_and_get_url(USER_RESET_PASSWORD)
            assert USER_RESET_PASSWORD in current_url, f"Не произошло перенаправление на {USER_RESET_PASSWORD}"

    @allure.title("Клик по иконке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_click_show_password_icon_activates_input(self, driver):
        recovery_page = PasswordRecoveryPage(driver)

        with allure.step("Пройти первый шаг восстановления и открыть форму /reset-password"):
            recovery_page.open_reset_page()

        with allure.step("Кликнуть на иконку глаза рядом в инпуте пароля"):
            recovery_page.click_show_password_button()

        with allure.step("Проверить, что поле подсветилось, type изменился на text"):
            input_type = recovery_page.get_password_input_type()
            container_classes = recovery_page.get_password_container_classes()
            
        assert input_type == "text" and "input_status_active" in container_classes, \
            f"Поле не активировано. Тип: '{input_type}', Классы контейнера: '{container_classes}'"
