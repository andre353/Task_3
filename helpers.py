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
    """Стабильный JS-скрипт для эмуляции HTML5 Drag and Drop в Chrome и Firefox"""
    js_script = """
    var source = arguments[0];
    var target = arguments[1];
    
    function createEvent(type) {
        var event = document.createEvent("CustomEvent");
        event.initCustomEvent(type, true, true, null);
        event.dataTransfer = {
            data: {},
            setData: function (type, val) { this.data.type = val; },
            getData: function (type) { return this.data.type; }
        };
        return event;
    }
    
    var dragStartEvent = createEvent('dragstart');
    source.dispatchEvent(dragStartEvent);
    
    var dragEnterEvent = createEvent('dragenter');
    target.dispatchEvent(dragEnterEvent);
    
    var dropEvent = createEvent('drop');
    dropEvent.dataTransfer = dragStartEvent.dataTransfer;
    target.dispatchEvent(dropEvent);
    
    var dragEndEvent = createEvent('dragend');
    source.dispatchEvent(dragEndEvent);
    """
    driver.execute_script(js_script, source_element, target_element)
