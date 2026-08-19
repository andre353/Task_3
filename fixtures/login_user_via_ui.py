import pytest
from endpoints.user_api import UserApi
from helpers import generate_user_payload
from urls import BASE_URL, USER_CABINET_LOGIN
from pages.base_page import BasePage
from locators.homepage_locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="function")
def login_user_via_ui(driver):
    base_page = BasePage(driver)
    user_api = UserApi(BASE_URL)
    
    # Cоздаем пользователя через API
    user_data = generate_user_payload()
    response = user_api.register_user(user_data)
    # Вызовет ошибку окружения, если API лежит или вернул плохой статус
    response.raise_for_status()
    
    response_data = response.json()
    token = response_data.get("accessToken")

    # Вход через UI под уже созданным пользователем
    driver.get(f"{BASE_URL}{USER_CABINET_LOGIN}")
    base_page.send_keys(HomePageLocators.LOGIN_EMAIL_INPUT, user_data["email"])
    base_page.send_keys(HomePageLocators.LOGIN_PASSWORD_INPUT, user_data["password"])
    base_page.scroll_to(HomePageLocators.LOGIN_SUBMIT_BUTTON)
    base_page.js_click(HomePageLocators.LOGIN_SUBMIT_BUTTON)
    
    # Ожидание токена в localStorage
    WebDriverWait(driver, 15).until(
        lambda d: d.execute_script("return window.localStorage.getItem('accessToken');") is not None,
        message="Токен авторизации не появился в localStorage после клика Войти"
    )
    
    driver.refresh()
    
    # Возвращаем данные в тест и настраиваем Teardown (удаление)
    yield user_data
    
    # Чистим базу данных после теста
    if token:
        user_api.delete_user(headers={"Authorization": token})




