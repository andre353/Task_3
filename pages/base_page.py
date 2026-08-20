from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urls import BASE_URL


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def wait_visible(self, locator):
        """Ожидает появления элемента в DOM и его видимости на странице"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_all_elements(self, locator):
        """Ожидает появления всех элементов списка в DOM"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_all_visible(self, locator):
        """Ожидает, что все элементы списка станут видимыми"""
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_clickable(self, locator):
        """Ожидает, пока элемент станет кликабельным"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find(self, locator):
        """Быстрый поиск элемента в DOM-дереве"""
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """Быстрый поиск списка элементов в DOM-дереве"""
        return self.driver.find_elements(*locator)

    def scroll_to(self, locator):
        """Прокручивает страницу до элемента, центрируя его на экране"""
        element = self.wait_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def click(self, locator):
        """Ожидает кликабельности элемента и кликает по нему"""
        self.wait_clickable(locator).click()

    def js_click(self, locator_or_element):
        """Выполняет клик по элементу силами JavaScript (при перекрытии)"""
        if isinstance(locator_or_element, tuple):
            element = self.find(locator_or_element)
        else:
            element = locator_or_element
        self.driver.execute_script("arguments[0].click();", element)

    def click_body(self):
        """Кликает по свободному месту страницы"""
        body = self.driver.find_element(By.TAG_NAME, "body")
        self.js_click(body)

    def send_keys(self, locator, text):
        """Универсальный метод ввода текста: ждет видимости поля и передает строку"""
        self.wait_visible(locator).send_keys(text)

    def get_current_url(self):
        """Возвращает текущий URL адрес браузера"""
        return self.driver.current_url

    def wait_for_url(self, expected_url):
        """Ожидание частичного или полного совпадения URL адреса"""
        return self.wait.until(EC.url_contains(expected_url))

    def wait_and_get_url(self, expected_part):
        """Ждет появление части ожидаемого URL и возвращает текущий URL"""
        self.wait_for_url(expected_part)
        return self.get_current_url()

    def go_home(self):
        """Переходит на главную страницу Stellar Burgers"""
        self.driver.get(BASE_URL)

