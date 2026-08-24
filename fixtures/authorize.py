import requests
import pytest
from urls import BASE_URL
from helpers import generate_user_payload


@pytest.fixture(scope="function")
def login_user(driver):
    payload = generate_user_payload()
    response = requests.post(f"{BASE_URL}/api/auth/register", json=payload)
    data = response.json()
    
    access_token = data.get("accessToken")
    refresh_token = data.get("refreshToken")
    
    # Открываем домен, чтобы получить контекст для localStorage
    driver.get(BASE_URL)
    
    # Прописываем токены
    driver.execute_script(f"window.localStorage.setItem('accessToken', '{access_token}');")
    driver.execute_script(f"window.localStorage.setItem('refreshToken', '{refresh_token}');")
    
    # Перезагружаем страницу, мы авторизованы
    driver.refresh()
    
    yield data
    
    # Очистка данных после теста
    if access_token:
        requests.delete(f"{BASE_URL}/api/auth/user", headers={"Authorization": access_token})

    driver.refresh()

