import pytest
from urls import BASE_URL, USER_CABINET_LOGIN
from helpers import generate_user_payload
from pages.base_page import BasePage
from locators.homepage_locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def login_user_via_ui(driver):
    """Надежная UI-фикстура авторизации с ожиданием токенов в памяти браузера"""
    base_page = BasePage(driver)
    user_data = generate_user_payload()
    
    # 1. Регистрация через UI
    driver.get(f"{BASE_URL}/register")
    base_page.send_keys(HomePageLocators.REG_NAME_INPUT, user_data["name"])
    base_page.send_keys(HomePageLocators.REG_EMAIL_INPUT, user_data["email"])
    base_page.send_keys(HomePageLocators.REG_PASSWORD_INPUT, user_data["password"])
    base_page.js_click(HomePageLocators.REG_SUBMIT_BUTTON)

    # 2. Вход через UI
    driver.get(f"{BASE_URL}{USER_CABINET_LOGIN}")
    base_page.send_keys(HomePageLocators.LOGIN_EMAIL_INPUT, user_data["email"])
    base_page.send_keys(HomePageLocators.LOGIN_PASSWORD_INPUT, user_data["password"])
    base_page.scroll_to(HomePageLocators.LOGIN_SUBMIT_BUTTON)
    base_page.js_click(HomePageLocators.LOGIN_SUBMIT_BUTTON)
    
    # 3. КРИТИЧЕСКИЙ ШАГ: Ждем, пока фронтенд сайта запишет accessToken в localStorage
    from selenium.webdriver.support.ui import WebDriverWait
    WebDriverWait(driver, 15).until(
        lambda d: d.execute_script("return window.localStorage.getItem('accessToken');") is not None,
        message="Токен авторизации не появился в localStorage после клика Войти"
    )
    
    # На всякий случай делаем жесткий рефреш, чтобы закрепить авторизованный статус сессии
    driver.refresh()
    
    yield user_data




