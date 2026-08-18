import pytest

# Регистрируем файлы с фикстурами, чтобы pytest автоматически их увидел
pytest_plugins = [
    "fixtures.drivers",
    "fixtures.home_page",
    "fixtures.authorize",
]

def pytest_addoption(parser):
    # Регистрируем новый аргумент командной строки для динамического выбора браузера
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Браузер для запуска тестов: chrome или firefox"
    )
