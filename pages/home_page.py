import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.homepage_locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from helpers import drag_and_drop_html5


class HomePage(BasePage):
    
    @allure.step("Открыть главную страницу Stellar Burgers через навигацию хедера")
    def open_home_page(self):
        from locators.homepage_locators import HomePageLocators
        try:
            self.click(HomePageLocators.CONSTRUCTOR_HEADER_BUTTON)
        except Exception:
            # Если мы и так на главной и кнопки нет — просто идем дальше
            self.go_home()

    @allure.step("Кликнуть на ингредиент для открытия модального окна")
    def click_ingredient(self):
        self.js_click(HomePageLocators.INGREDIENT)

    @allure.step("Проверить, что всплывающее окно с деталями отображается")
    def is_popup_displayed(self):
        return self.wait_visible(HomePageLocators.POPUP).is_displayed()

    @allure.step("Кликнуть по крестику для закрытия всплывающего окна")
    def click_close_popup_button(self):
        self.js_click(HomePageLocators.POPUP_CLOSE_BUTTON)

    @allure.step("Проверить, что всплывающее окно закрылось (отсутствует в DOM или скрыто)")
    def is_popup_closed(self):
        from selenium.webdriver.support import expected_conditions as EC
        try:
            self.wait.until(EC.invisibility_of_element_located(HomePageLocators.POPUP))
            return True
        except Exception:
            return False

    @allure.step("Получить текущее значение каунтера ингредиента")
    def get_ingredient_counter_value(self):
        element = self.wait_visible(HomePageLocators.INGREDIENT_COUNTER)
        return int(element.text)

    @allure.step("Кликнуть по кнопке 'Оформить заказ'")
    def click_place_order_button(self):
        button = self.wait_clickable(HomePageLocators.PLACE_ORDER_BUTTON)
        button.click()

    @allure.step("Оформить заказ через UI (Drag and Drop и клик)")
    def create_order_via_ui(self):
        
        # Находим элементы на странице
        ingredient_el = self.wait_visible(HomePageLocators.INGREDIENT)
        target_el = self.wait_visible((By.XPATH, "//button[contains(text(), 'заказ') or contains(text(), 'Войти')]"))
        
        # Выполняем Drag and Drop
        drag_and_drop_html5(self.driver, ingredient_el, target_el)
        
        # Браузеру необходимо время завершить выполнение JS-скриптов и обновить состояние кнопки (специфика React)
        self.wait_clickable(target_el) 
        
        # Кликаем по кнопке оформления заказа
        target_el.click()

    @allure.step("Получить ID заказа из всплывающего окна подтверждения")
    def get_popup_order_id(self):
        # Сначала просто дожидаемся физического появления окна на экране
        self.wait_visible(HomePageLocators.POPUP_ORDER_ID)
        
        # Создаем локальный wait с игнорированием StaleElement ошибок
        secure_wait = WebDriverWait(
            self.driver, 
            timeout=15, 
            ignored_exceptions=(StaleElementReferenceException,)
        )
        
        # Запускаем безопасный цикл проверки текста
        secure_wait.until(
            lambda d: d.find_element(*HomePageLocators.POPUP_ORDER_ID).text.strip() not in ["9999", ""],
            message="Бэкенд не заменил заглушку '9999' на реальный номер заказа за 15 секунд"
        )
        
        # Финально забираем уже сгенерированный ID
        return self.driver.find_element(*HomePageLocators.POPUP_ORDER_ID).text.strip()

    @allure.step("Дождаться, пока каунтер ингредиента увеличится по сравнению со стартовым")
    def wait_for_ingredient_counter_to_change(self, initial_value):
        # Метод вернет True, как только число в каунтере станет больше initial_value
        return self.wait.until(
            lambda d: int(d.find_element(*HomePageLocators.INGREDIENT_COUNTER).text) > initial_value
        )
    




