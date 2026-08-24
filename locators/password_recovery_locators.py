from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:

    RECOVER_PASSWORD_BUTTON = (By.CSS_SELECTOR, "a[href='/forgot-password']")
    RECOVER_PASSWORD_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RECOVER_PASSWORD_FORM_BUTTON = (By.CSS_SELECTOR, "form[class*='Auth_form'] button")
    # /reset-password
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    SHOW_PASSWORD_INPUT_BUTTON = (By.CSS_SELECTOR, "div.input__icon-action")
    EMAIL_INPUT = (By.XPATH, "//input[@type='text' or @name='name']") 
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']") 

