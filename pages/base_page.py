import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from locators.base_locators import BaseLocators
from urls import BASE_URL


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    # ----------------------------------------------------------------
    # Базовые методы поиска и базовые ожидания
    # ----------------------------------------------------------------

    def find(self, locator):
        """Быстрый поиск одного элемента в DOM-дереве."""
        return self.driver.find_element(*locator)

    def wait_visible(self, locator):
        """Ожидает появления элемента в DOM и его видимости на странице."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_all_visible(self, locator, timeout=5):
        """Ожидает, пока все элементы списка станут видимыми на экране."""
        secure_wait = WebDriverWait(self.driver, timeout)
        return secure_wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_clickable(self, locator):
        """Ожидает, пока элемент станет кликабельным."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_url(self, expected_url):
        """Ожидает частичного или полного совпадения URL-адреса браузера."""
        return self.wait.until(EC.url_contains(expected_url))

    # ----------------------------------------------------------------
    # Универсальные действия с элементами и навигация
    # ----------------------------------------------------------------

    def click(self, locator):
        """Ожидает кликабельности элемента и кликает по нему стандартным способом."""
        self.wait_clickable(locator).click()

    def js_click(self, locator_or_element):
        """Выполняет принудительный клик по элементу через JavaScript (при перекрытии)."""
        if isinstance(locator_or_element, tuple):
            element = self.find(locator_or_element)
        else:
            element = locator_or_element
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text):
        """Универсальный метод ввода текста: ждет видимости поля и передает строку."""
        self.wait_visible(locator).send_keys(text)

    def scroll_to(self, locator):
        """Прокручивает страницу до элемента, центрируя его на экране."""
        element = self.wait_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def click_body(self):
        """Кликает по свободному месту страницы (тегу body) для снятия фокуса."""
        body = self.driver.find_element(By.TAG_NAME, "body")
        self.js_click(body)

    def navigate_to(self, url):
        """Открывает указанную веб-страницу в браузере."""
        self.driver.get(url)

    def get_current_url(self):
        """Возвращает текущий URL-адрес браузера."""
        return self.driver.current_url

    def refresh_page_via_js(self):
        """Принудительно обновляет страницу через JavaScript с очисткой кэша вкладки."""
        self.driver.execute_script("location.reload(true);")

    def wait_invisible(self, locator):
        """Ожидает, пока элемент полностью исчезнет с экрана."""
        return self.wait.until(EC.invisibility_of_element_located(locator))    

    # ----------------------------------------------------------------
    # Переходы по страницам и клики в хедере
    # ----------------------------------------------------------------

    @allure.step("Открыть главную страницу Stellar Burgers")
    def open_home_page(self):
        """
        Переход по URL, если мы не на главной. 
        Если уже на главной — выполняет клик по логотипу.
        """
        try:
            # Проверяем на уровне браузера, является ли текущий URL главной страницей
            WebDriverWait(self.driver, 0.5).until(EC.url_to_be(BASE_URL))
            
            # Если мы на главной, то кликаем по логотипу
            self.click(BaseLocators.LOGO_LINK)
            
        except TimeoutException:
            # Во остальных случаях осуществляется переход по url
            self.navigate_to(BASE_URL)

    @allure.step("Открыть главную страницу Stellar Burgers через клик на меню 'Конструктор'")
    def open_home_page_via_constructor_link(self):
        """Выполняет прямой линейный клик по вкладке Конструктора в хедере."""
        self.click(BaseLocators.CONSTRUCTOR_HEADER_LINK)

    @allure.step("Открыть страницу 'Лента заказов' через навигацию хедера")
    def open_orders_feed_page_via_feed_link(self):
        """Выполняет клик по кнопке перехода в Ленту заказов."""
        self.click(BaseLocators.ORDERS_FEED_PAGE_LINK)    

    # ----------------------------------------------------------------
    # Продвинутые кастомные ожидания для динамических компонентов
    # ----------------------------------------------------------------

    def wait_for_text_not_in_exceptions(self, locator, bad_texts, timeout=15):
        """
        Ждет, пока текст элемента изменится с дефолтных заглушек.
        Возвращает финальный текст. Игнорирует StaleElementReferenceException.
        """
        secure_wait = WebDriverWait(
            self.driver,
            timeout=timeout,
            ignored_exceptions=(StaleElementReferenceException,)
        )
        
        secure_wait.until(
            lambda d: d.find_element(*locator).text.strip() not in bad_texts,
            message=f"Текст элемента {locator} не обновился за {timeout} секунд"
        )
        
        return self.find(locator).text.strip()

    def wait_for_numeric_value_to_increase(self, locator, initial_value, timeout=10):
        """Ожидает, пока числовое значение счетчика/каунтера станет больше стартового."""
        secure_wait = WebDriverWait(self.driver, timeout)
        return secure_wait.until(
            lambda d: int(d.find_element(*locator).text.strip()) > initial_value
        )

    def get_elements_with_retry_on_refresh(self, locator, url_trigger_text, initial_timeout=3):
        """
        Ждет нужный URL, пытается найти список элементов.
        Если они не отрисовались за initial_timeout, делает рефреш через JS и находит их гарантированно.
        """
        self.wait_for_url(url_trigger_text)
        
        try:
            return WebDriverWait(self.driver, initial_timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            self.refresh_page_via_js()
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(locator)
            )

    def wait_for_child_text_to_change(self, parent_element, child_locator, initial_value, timeout=10):
        """Ожидает, пока числовое значение внутри дочернего элемента увеличится."""
        
        return WebDriverWait(self.driver, timeout).until(
            lambda d: int(parent_element.find_element(*child_locator).text.strip()) > initial_value
        )
