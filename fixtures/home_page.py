import pytest
from pages.home_page import HomePage
from urls import BASE_URL


@pytest.fixture
def home_page(driver):
    driver.get(BASE_URL)
    return HomePage(driver)