from selenium.webdriver.common.by import By


class HomePageLocators:

    INGREDIENT = (By.CSS_SELECTOR, "a[class*='BurgerIngredient_ingredient']")
    POPUP = (By.CSS_SELECTOR, "section[class*='modal_opened']")
    POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, "section[class*='modal_opened'] button[class*='modal__close']")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "p[class*='counter__num']")
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, "button.button_button__31Z_m")
    POPUP_ORDER_ID = (By.CSS_SELECTOR, "section[class*='modal_opened'] h2[class*='modal__title']")
    FEED_ORDER_ITEMS = (By.CSS_SELECTOR, "li[class*='OrderHistory_listItem']") 
    FEED_ORDER_ID = (By.CSS_SELECTOR, "ul[class*='OrderFeed_list'] p[class*='text_type_digits']")


