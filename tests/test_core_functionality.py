import pytest
import allure
from locators.homepage_locators import HomePageLocators
from pages.home_page import HomePage
from helpers import generate_user_payload, drag_and_drop_html5 


@allure.suite("Основной функционал главной страницы")
class TestCoreFunctionality:

    @allure.title("Появление всплывающего окна с деталями при клике на ингредиент")
    def test_click_ingredient_opens_popup_details(self, driver):
        home_page = HomePage(driver)

        with allure.step("Открыть главную страницу и кликнуть на ингредиент"):
            home_page.open_home_page()
            home_page.click_ingredient()
        
        assert home_page.is_popup_displayed(), "Всплывающее окно с деталями ингредиента не открылось!"

    @allure.title("Всплывающее окно успешно закрывается при клике на крестик")
    def test_click_close_icon_closes_popup(self, driver):
        home_page = HomePage(driver)
        
        with allure.step("Открыть главную страницу, кликнуть на ингредиент и закрыть модальное окно"):
            home_page.open_home_page()
            home_page.click_ingredient()
            home_page.click_close_popup_button()
        
        assert home_page.is_popup_closed(), "Всплывающее окно не закрылось после клика на крестик!"

    @allure.title("При добавлении ингредиента в заказ увеличивается его каунтер")
    def test_adding_ingredient_increments_counter(self, driver):
        home_page = HomePage(driver)
        
        with allure.step("Открыть главную страницу и зафиксировать начальное значение каунтера"):
            home_page.open_home_page()
            initial_counter = home_page.get_ingredient_counter_value()

        with allure.step("Перетащить ингредиент в конструктор бургеров"):
            ingredient_el = home_page.wait_visible(HomePageLocators.INGREDIENT)
            target_el = home_page.wait_visible(HomePageLocators.BURGER_CONSTRUCTOR_BASKET)
            
            drag_and_drop_html5(driver, ingredient_el, target_el)
            
            counter_increased = home_page.wait_for_ingredient_counter_to_change(initial_counter)

        assert counter_increased, f"Каунтер ингредиента не увеличился! Стартовое значение: {initial_counter}"

    @allure.title("Залогиненный пользователь может успешно оформить заказ")
    def test_authorized_user_can_place_order(self, driver, login_user_via_ui):
        home_page = HomePage(driver)
            
        with allure.step("Открыть главную страницу и оформить заказ через интерфейс Конструктора"):
            home_page.open_home_page()
            home_page.create_order_via_ui()

        with allure.step("Считать сгенерированный ID заказа из модального окна"):
            order_id = home_page.get_popup_order_id()

        assert order_id != "9999" and order_id.strip() != "", f"Заказ не оформился, возвращен некорректный ID: {order_id}"
        

