import pytest
import allure
from pages.orders_feed_page import OrdersFeedPage
from pages.home_page import HomePage


@allure.suite("Лента заказов (Только UI)")
class TestOrdersFeed:

    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_click_order_opens_popup_details(self, driver):
        feed_page = OrdersFeedPage(driver)
        home_page = HomePage(driver)

        feed_page.open_feed_page()
        feed_page.click_first_order()

        assert home_page.is_popup_displayed(), "Всплывающее окно с деталями заказа не открылось при клике!"

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_new_order_appears_in_progress_section(self, driver, login_user_via_ui):
        feed_page = OrdersFeedPage(driver)
        home_page = HomePage(driver)

        with allure.step("Оформить заказ через интерфейс Конструктора и зафиксировать его ID"):
            home_page.open_home_page()
            home_page.create_order_via_ui()
            
            order_number = home_page.get_popup_order_id()
            home_page.click_close_popup_button()

        with allure.step("Перейти в Ленту заказов и проверить раздел 'В работе'"):
            feed_page.open_feed_page()
            
            # Принудительно сбрасываем кэш вкладки для принудительного обновления стейта сокетов ленты
            driver.execute_script("location.reload(true);")
            
            orders_in_progress = feed_page.get_orders_in_progress()
            short_order_id = order_number.lstrip('0')

            assert any(short_order_id in order for order in orders_in_progress), \
                f"Заказ {order_number} не найден в списке 'В работе'. Доступные номера: {orders_in_progress}"

    @allure.title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_all_time_counter_increments_on_new_order(self, driver, login_user_via_ui):
        feed_page = OrdersFeedPage(driver)
        home_page = HomePage(driver)

        with allure.step("Зафиксировать начальное значение счетчика 'За все время'"):
            feed_page.open_feed_page()
            initial_all_time = feed_page.get_all_time_counter_value()

        with allure.step("Оформить заказ через интерфейс Конструктора"):
            home_page.open_home_page()
            home_page.create_order_via_ui()
            home_page.click_close_popup_button()

        with allure.step("Вернуться в Ленту заказов и дождаться изменения счетчика"):
            feed_page.open_feed_page()
            # Принудительно сбрасываем кэш сокетов
            driver.execute_script("location.reload(true);")
            
            # Метод ожидания возвращает True, когда и если число счетчика вырастет
            counter_increased = feed_page.wait_for_all_time_counter_to_change(initial_all_time)

        assert counter_increased, f"Счетчик 'За все время' не увеличился! Начальное значение: {initial_all_time}"

    @allure.title("При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_counter_increments_on_new_order(self, driver, login_user_via_ui):
        feed_page = OrdersFeedPage(driver)
        home_page = HomePage(driver)

        with allure.step("Зафиксировать начальное значение счетчика 'За сегодня'"):
            feed_page.open_feed_page()
            initial_today = feed_page.get_today_counter_value()

        with allure.step("Оформить заказ через интерфейс Конструктора"):
            home_page.open_home_page()
            home_page.create_order_via_ui()
            home_page.click_close_popup_button()

        with allure.step("Вернуться в Ленту заказов и дождаться изменения счетчика"):
            feed_page.open_feed_page()
            driver.execute_script("location.reload(true);")
            
            # Ждем изменения счетчика относительно зафиксированного начального значения
            counter_increased = feed_page.wait_for_today_counter_to_change(initial_today)

        assert counter_increased, f"Счетчик 'За сегодня' не увеличился! Начальное значение: {initial_today}"



