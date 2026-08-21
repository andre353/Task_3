import allure
from pages.base_page import BasePage
from locators.orders_feed_locators import OrdersFeedLocators
from locators.homepage_locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL, ORDERS_FEED        


class OrdersFeedPage(BasePage):

    @allure.step("Открыть страницу 'Лента заказов'")
    def open_feed_page(self):
        self.navigate_to(f"{BASE_URL}{ORDERS_FEED}")

    @allure.step("Кликнуть по первому заказу в ленте")
    def click_first_order(self):
        self.click(HomePageLocators.FEED_ORDER_ITEMS)

    @allure.step("Получить значение счетчика 'Выполнено за все время'")
    def get_all_time_counter_value(self):
        element = self.wait_visible(OrdersFeedLocators.DONE_FOR_ALL_TIME_COUNTER)
        return int(element.text)

    @allure.step("Получить значение счетчика 'Выполнено за сегодня'")
    def get_today_counter_value(self):
        element = self.wait_visible(OrdersFeedLocators.DONE_TODAY_COUNTER)
        return int(element.text)

    @allure.step("Дождаться, пока счетчик 'Выполнено за все время' увеличится по сравнению со стартовым")
    def wait_for_all_time_counter_to_change(self, initial_value):
        # Метод вернет True, как только число в DOM станет больше initial_value
        return self.wait.until(
            lambda d: int(d.find_element(*OrdersFeedLocators.DONE_FOR_ALL_TIME_COUNTER).text) > initial_value
        )

    @allure.step("Дождаться, пока счетчик 'Выполнено за сегодня' увеличивается по сравнению со стартовым")
    def wait_for_today_counter_to_change(self, initial_value):
        # Метод вернет True, как только число в DOM станет больше initial_value
        return self.wait.until(
            lambda d: int(d.find_element(*OrdersFeedLocators.DONE_TODAY_COUNTER).text) > initial_value
        )    

    @allure.step("Получить список номеров всех заказов из раздела 'В работе'")
    def get_orders_in_progress(self):
        elements = self.wait_all_visible(OrdersFeedLocators.ORDERS_IN_PROGRESS_LIST)
        return [el.text for el in elements]

        


