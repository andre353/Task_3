from selenium.webdriver.common.by import By


class UserCabinetLocators:

    ORDERS_HISTORY_BUTTON = (By.CSS_SELECTOR, "ul[class*='Account_list'] a[href='/account/order-history']")
    USER_EXIT_BUTTON = (By.CSS_SELECTOR, "ul[class*='Account_list'] button")

