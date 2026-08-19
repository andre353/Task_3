from selenium.webdriver.common.by import By


class HomePageLocators:

    INGREDIENT = (By.CSS_SELECTOR, "a[class*='BurgerIngredient_ingredient']")
    POPUP = (By.CSS_SELECTOR, "section[class*='modal_opened']")
    POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, "section[class*='modal_opened'] button[class*='modal__close']")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "p[class*='counter__num']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    POPUP_ORDER_ID = (By.CSS_SELECTOR, "section[class*='modal_opened'] h2[class*='modal__title']")
    FEED_ORDER_ITEMS = (By.CSS_SELECTOR, "li[class*='OrderHistory_listItem']") 
    FEED_ORDER_ID = (By.CSS_SELECTOR, "ul[class*='OrderFeed_list'] p[class*='text_type_digits']")
    # --- Элемент Конструктора бургера (/) ---
    BURGER_CONSTRUCTOR_BASKET = (By.CSS_SELECTOR, "section[class*='BurgerConstructor_basket']")

    # --- Элементы формы Регистрации (/register) ---
    REG_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    REG_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    REG_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REG_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # --- Элементы формы Авторизации (/login) ---
    LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")

    CONSTRUCTOR_HEADER_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")

