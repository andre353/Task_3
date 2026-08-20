from selenium.webdriver.common.by import By


class UserCabinetLocators:

    ORDERS_HISTORY_BUTTON = (By.CSS_SELECTOR, "ul[class*='Account_list'] a[href='/account/order-history']")
    ORDERS_HISTORY_NUMBERS = (By.XPATH, "//p[starts-with(text(), '#')]")
    USER_EXIT_BUTTON = (By.CSS_SELECTOR, "ul[class*='Account_list'] button")

