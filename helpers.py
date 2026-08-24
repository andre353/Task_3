import random
import string


def generate_random_string(length=10):
    """Генерирует случайную строку из строчных латинских букв."""
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))

def generate_user_payload():
    """
    Генерирует валидные данные для регистрации нового пользователя (/api/auth/register).
    """
    return {
        "email": f"test_{generate_random_string(8)}@yandex.ru",
        "password": generate_random_string(10),
        "name": f"User_{generate_random_string(5)}"
    }

def drag_and_drop_html5(driver, source_element, target_element):
    """JS-скрипт для эмуляции HTML5 Drag and Drop"""
    js_script = """
    var source = arguments[0];
    var target = arguments[1];
    
    // Используем современный конструктор DataTransfer, который требует React-DnD в Firefox
    var dataTransfer = new DataTransfer();
    
    function createEvent(type) {
        var event = new DragEvent(type, {
            bubbles: true,
            cancelable: true,
            dataTransfer: dataTransfer
        });
        return event;
    }
    
    // Полноценная цепочка событий drag & drop
    source.dispatchEvent(createEvent('dragstart'));
    target.dispatchEvent(createEvent('dragenter'));
    target.dispatchEvent(createEvent('dragover'));
    target.dispatchEvent(createEvent('drop'));
    source.dispatchEvent(createEvent('dragend'));
    """
    driver.execute_script(js_script, source_element, target_element)

