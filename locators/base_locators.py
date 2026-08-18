from selenium.webdriver.common.by import By


class BaseLocators:
    # Menu/Header locators
    LOGO_LINK = (By.CSS_SELECTOR, "nav div[class*='logo'] > a")
    CONSTRUCTOR_MAIN_PAGE_LINK = (By.XPATH, "//nav//ul[contains(@class, '_list_')]/a[@href='/']//*[contains(text(), 'Конструктор')]")
    ORDERS_FEED_PAGE_LINK = (By.CSS_SELECTOR, "nav ul[class*='list'] > a[href='/feed']")
    ACCOUNT_PAGE_LINK = (By.CSS_SELECTOR, "nav > a[href='/account']")
