import pytest
import allure
from pages.user_cabinet_page import UserCabinetPage
from urls import USER_CABINET, USER_ORDER_HISTORY


@allure.suite("Личный кабинет")
class TestUserCabinet:

    @allure.title("Переход по клику на 'Личный кабинет'")
    def test_navigation_to_user_cabinet(self, driver, login_user):
        cabinet_page = UserCabinetPage(driver)

        cabinet_page.click_header_cabinet_button()

        cabinet_page.wait_for_url(USER_CABINET)
        current_url = cabinet_page.get_current_url()
        assert USER_CABINET in current_url, f"Перейти в ЛК не удалось. Текущий URL: {current_url}"

    @allure.title("Переход в раздел 'История заказов'")
    def test_navigation_to_orders_history(self, driver, login_user):
        cabinet_page = UserCabinetPage(driver)

        # Переходим в личный кабинет
        cabinet_page.click_header_cabinet_button()
        # Переходим в историю заказов
        cabinet_page.click_orders_history_button()

        cabinet_page.wait_for_url(USER_ORDER_HISTORY)
        current_url = cabinet_page.get_current_url()
        assert USER_ORDER_HISTORY in current_url, f"Секция 'История заказов' не открылась. URL: {current_url}"

    @allure.title("Выход из аккаунта")
    def test_user_logout(self, driver, login_user):
        cabinet_page = UserCabinetPage(driver)

        # Переходим в личный кабинет
        cabinet_page.click_header_cabinet_button()
        # Кликаем "Выход"
        cabinet_page.click_exit_button()
        
        is_login_page = cabinet_page.wait_for_login_page_load()
        assert is_login_page, "После выхода из аккаунта пользователь не был перенаправлен на страницу входа."
