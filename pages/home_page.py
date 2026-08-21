import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.homepage_locators import HomePageLocators
from locators.base_locators import BaseLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from helpers import drag_and_drop_html5


class HomePage(BasePage):

    # ----------------------------------------------------------------
    # Взаимодействие с ингредиентами и модальными окнами
    # ----------------------------------------------------------------

    @allure.step("Кликнуть на ингредиент для открытия модального окна деталей")
    def click_ingredient(self):
        """Выполняет клик по карточке ингредиента через JavaScript."""
        self.wait_visible(HomePageLocators.INGREDIENT)
        self.js_click(HomePageLocators.INGREDIENT)

    @allure.step("Проверить, что всплывающее окно с деталями отображается")
    def is_popup_displayed(self):
        """Возвращает True, если окно успешно появилось на экране."""
        return bool(self.wait_visible(HomePageLocators.POPUP))

    @allure.step("Кликнуть по крестику для закрытия всплывающего окна")
    def click_close_popup_button(self):
        """Закрывает модальное окно принудительным JS-кликом по крестику."""
        self.js_click(HomePageLocators.POPUP_CLOSE_BUTTON)

    @allure.step("Проверить, что всплывающее окно с деталями закрылось")
    def is_popup_closed(self):
        """Возвращает True, если модальное окно успешно исчезло из DOM/экрана."""
        return bool(self.wait_invisible(HomePageLocators.POPUP))    

    @allure.step("Получить текущее значение каунтера ингредиента")
    def get_ingredient_counter_value(self):
        """Считывает текстовое значение счетчика и возвращает его как целое число."""
        element = self.wait_visible(HomePageLocators.INGREDIENT_COUNTER)
        return int(element.text.strip())

    @allure.step("Дождаться, пока каунтер ингредиента увеличится по сравнению со стартовым")
    def wait_for_ingredient_counter_to_change(self, initial_value):
        """Использует продвинутое ожидание из BasePage для отслеживания изменения счетчика."""
        ingredient_element = self.wait_visible(HomePageLocators.INGREDIENT)
        
        # Передаем элемент и локатор счетчика в базовое ожидание
        return self.wait_for_child_text_to_change(
            parent_element=ingredient_element,
            child_locator=HomePageLocators.INGREDIENT_COUNTER,
            initial_value=initial_value
        )

    # ----------------------------------------------------------------
    # Бизнес-логика оформления заказа через UI
    # ----------------------------------------------------------------

    @allure.step("Кликнуть по кнопке 'Оформить заказ'")
    def click_place_order_button(self):
        """Кликает по кнопке оформления заказа стандартным способом."""
        self.click(HomePageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Оформить заказ через UI (Drag and Drop и клик)")
    def create_order_via_ui(self):
        """
        Выполняет комплексный сценарий: ожидает элементы, перетаскивает ингредиент 
        в корзину конструктора с помощью HTML5-скрипта и кликает по кнопке оформления.
        """
        source_element = self.wait_visible(HomePageLocators.INGREDIENT)
        target_element = self.wait_visible(HomePageLocators.BURGER_CONSTRUCTOR_BASKET)
        
        drag_and_drop_html5(self.driver, source_element, target_element)        
        self.js_click(HomePageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Получить ID заказа из всплывающего окна подтверждения")
    def get_popup_order_id(self):
        """
        Дожидается обновления текста в окне подтверждения заказа,
        пропуская дефолтные заглушки вроде '9999' или пустые строки.
        """
        order_id = self.wait_for_text_not_in_exceptions(
            locator=HomePageLocators.POPUP_ORDER_ID,
            bad_texts=["9999", ""]
        )
        return order_id
    
