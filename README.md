# Task_3 Проект автоматизации тестирования сайта учебного сервиса 

1. Основа для написания автотестов Selenium, pytest.
2. Применена Page Object Model.
3. Подключен Allure-отчёт.
4. Установить зависимости — `pip install -r requirements.txt`
5. Команда для запуска тестов — `pytest -v`
6. Команда для запуска тестов с allure — `pytest`
7. По умолчанию тесты запускаются в **Chrome**. Вы можете явно указать браузер с помощью флага `--browser`:

*   **Запуск в Chrome (по умолчанию):**
    ```bash
    pytest -v --browser=chrome
    ```
*   **Запуск в Firefox:**
    ```bash
    pytest -v --browser=firefox
    ```

8. Команда генерации статического отчета - `allure generate allure-results --clean -o my-report`
9. Команда для открытия отчета через сервер в браузере - `allure open my-report`
