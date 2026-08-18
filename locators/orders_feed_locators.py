from selenium.webdriver.common.by import By


class OrdersFeedLocators:

    DONE_FOR_ALL_TIME_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DONE_TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDERS_IN_PROGRESS_LIST = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul[1]/li")
