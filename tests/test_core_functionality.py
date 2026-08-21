import pytest
import allure
from locators.base_locators import BaseLocators
from locators.homepage_locators import HomePageLocators
from pages.base_page import BasePage
from pages.home_page import HomePage
from helpers import generate_user_payload, drag_and_drop_html5 
from urls import BASE_URL, ORDERS_FEED


@allure.suite("Проверка основного функционала")
class TestCoreFunctionality:

    @allure.title("Переход по клику на 'Конструктор'")
    def test_click_constructor_opens_constructor_page(self, driver):
        home_page = HomePage(driver)        
        home_page.navigate_to(f"{BASE_URL}{ORDERS_FEED}")            
        home_page.click(BaseLocators.CONSTRUCTOR_HEADER_LINK)
            
        assert home_page.get_current_url().rstrip('/') == BASE_URL, (
            f"Ожидалась главная страница {BASE_URL}, но открыт адрес: {home_page.get_current_url()}"
        )

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_click_order_feed_opens_order_feed_page(self, driver):
        home_page = HomePage(driver)        
        home_page.navigate_to(BASE_URL)            
        home_page.click(BaseLocators.ORDERS_FEED_PAGE_LINK)           
        expected_url = f"{BASE_URL}{ORDERS_FEED}"

        assert home_page.get_current_url() == expected_url, f"Ожидался URL {expected_url}, но получили {home_page.get_current_url()}"

    @allure.title("Если кликнуть на ингридиент, появится всплывающее окно с деталями")
    def test_click_ingredient_opens_popup_details(self, driver):
        home_page = HomePage(driver)

        with allure.step("Открыть главную страницу и кликнуть на ингредиент"):
            home_page.open_home_page()
            home_page.click_ingredient()
        
        assert home_page.is_popup_displayed(), "Всплывающее окно с деталями ингредиента не открылось!"

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_click_close_icon_closes_popup(self, driver):
        home_page = HomePage(driver)
        
        with allure.step("Открыть главную страницу, кликнуть на ингредиент и закрыть модальное окно"):
            home_page.open_home_page()
            home_page.click_ingredient()
            home_page.click_close_popup_button()
        
        assert home_page.is_popup_closed(), "Всплывающее окно не закрылось после клика на крестик!"

    @allure.title("При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
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

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_authorized_user_can_place_order(self, driver, login_user_via_ui):
        home_page = HomePage(driver)
            
        with allure.step("Открыть главную страницу и оформить заказ через интерфейс Конструктора"):
            home_page.open_home_page()
            home_page.create_order_via_ui()

        with allure.step("Считать сгенерированный ID заказа из модального окна"):
            order_id = home_page.get_popup_order_id()

        assert order_id != "9999" and order_id.strip() != "", f"Заказ не оформился, возвращен некорректный ID: {order_id}"
        

