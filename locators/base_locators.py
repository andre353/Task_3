from selenium.webdriver.common.by import By


class BaseLocators:
    # Menu/Header locators
    LOGO_LINK = (By.CSS_SELECTOR, "nav div[class*='logo'] > a")
    CONSTRUCTOR_HEADER_LINK = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    ORDERS_FEED_PAGE_LINK = (By.XPATH, "//a[contains(@href, '/feed') and .//p[text()='Лента Заказов']]")
    HEADER_CABINET_BUTTON = (By.XPATH, "//a[contains(@href, '/account') or text()='Личный кабинет']")
    PARENT_ELEMENT = (By.XPATH, "./..")
