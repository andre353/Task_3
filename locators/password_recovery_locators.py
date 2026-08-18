from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:

    RECOVER_PASSWORD_BUTTON = (By.CSS_SELECTOR, "a[href='/forgot-password']")
    RECOVER_PASSWORD_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RECOVER_PASSWORD_FORM_BUTTON = (By.CSS_SELECTOR, "form[class*='Auth_form'] button")
    # /reset-password
    PASSWORD_INPUT = (By.XPATH, "//div[contains(@class, 'input_type_password')]//input")
    # PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']/parent::div")
    SHOW_PASSWORD_INPUT_BUTTON = (By.CSS_SELECTOR, "div.input__icon-action")
    # SHOW_PASSWORD_INPUT_BUTTON = (By.XPATH, "//input[@type='password']/following-sibling::div[contains(@class, 'input__icon')]")
