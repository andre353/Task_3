import pytest

# Регистрируем файлы с фикстурами, чтобы pytest автоматически их увидел
pytest_plugins = [
    "fixtures.drivers",
    "fixtures.home_page",
]

