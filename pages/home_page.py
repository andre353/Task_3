import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.homepage_locators import HomePageLocators


class HomePage(BasePage):
    
    @allure.step("Открыть главную страницу Stellar Burgers через навигацию хедера")
    def open_home_page(self):
        from locators.homepage_locators import HomePageLocators
        # Вместо self.go_home() используем клик по шапке, чтобы не сбросить сессию
        try:
            self.click(HomePageLocators.CONSTRUCTOR_HEADER_BUTTON)
        except Exception:
            # Если мы и так на главной и кнопки нет — просто идем дальше
            self.go_home()

    @allure.step("Кликнуть на ингредиент для открытия модального окна")
    def click_ingredient(self):
        self.click(HomePageLocators.INGREDIENT)

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
        self.click(HomePageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Получить ID заказа из всплывающего окна подтверждения")
    def get_popup_order_id(self):
        # Ждем появления заголовка с номером заказа, получаем текст - id
        element = self.wait_visible(HomePageLocators.POPUP_ORDER_ID)
        return element.text

    @allure.step("Оформить заказ чисто через UI (Drag and Drop и клик)")
    def create_order_via_ui(self):
        from locators.homepage_locators import HomePageLocators
        from selenium.webdriver.common.by import By
        from helpers import drag_and_drop_html5
        import time
        
        # Находим элементы на странице
        ingredient_el = self.wait_visible(HomePageLocators.INGREDIENT)
        target_el = self.wait_visible((By.XPATH, "//button[contains(text(), 'заказ') or contains(text(), 'Войти')]"))
        
        # Выполняем стабильный Drag and Drop
        drag_and_drop_html5(self.driver, ingredient_el, target_el)
        
        # Браузеру необходимо время завершить выполнение JS-скриптов и обновить состояние кнопки (специфика React)
        time.sleep(0.5)
        
        # Кликаем по кнопке оформления заказа
        target_el.click()

    @allure.step("Получить ID заказа из всплывающего окна подтверждения")
    def get_popup_order_id(self):
        from selenium.webdriver.support import expected_conditions as EC
        from locators.homepage_locators import HomePageLocators
        
        # Ждем появления элемента на экране
        element = self.wait_visible(HomePageLocators.POPUP_ORDER_ID)
        
        # Ждем, пока текст элемента перестанет отображать хардкодид "9999"
        # и пока не произойдет генерация реального ID
        self.wait.until(
            lambda d: d.find_element(*HomePageLocators.POPUP_ORDER_ID).text != "9999",
            message="Бэкенд не заменил заглушку '9999' на реальный номер заказа за 15 секунд"
        )
        
        # Возвращаем сгенерированный номер заказа
        return element.text




