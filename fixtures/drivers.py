import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class WebDriverFactory:
    @staticmethod
    def get_driver(browser_name: str):
        browser = browser_name.lower()
        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            options.set_capability("acceptInsecureCerts", True)
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = FirefoxOptions()
            options.set_preference("dom.webnotifications.enabled", False)
            options.set_preference("datareporting.policy.dataSubmissionEnabled", False)
            options.set_preference("app.update.enabled", False)
            options.accept_secure_certs = True
            driver = webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Браузер '{browser_name}' не поддерживается Фабрикой!")
        
        driver.maximize_window()
        return driver


@pytest.fixture(scope="function")
def driver(request):
    # Считываем имя браузера из команды терминала. Если не указан, chrome по умолчанию
    browser_name = request.config.getoption("--browser", default="chrome")
    
    driver = WebDriverFactory.get_driver(browser_name)
    
    yield driver
    driver.quit()
