from selenium.webdriver.common.by import By


class Locators:
    # Локаторы главной страницы
    LOGIN_BUTTON_MAIN = ("xpath", "//button[text()='Войти в аккаунт']") # Кнопка входа на главной странице
    PERSONAL_ACCOUNT_LINK = ("xpath", "//header//a[@href='/account']") # Кнопка перехода в личный кабинет
    LOGO = ("xpath", "//div[contains(@class, 'AppHeader_header__logo__')]") # Логотип Stella Burgers

    # Регистрация
    REG_BUTTON = ("xpath", "//button[text()='Зарегистрироваться']") # Кнопка регистрации
    REGISTRATION_BUTTON = ("xpath", "//a[text()='Зарегистрироваться']") # Кнопка регистрации в форме регистрации
    NAME = ("xpath", "//input[@name='name']") # Поле ввода имени
    EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input") # Поле ввода email
    PASSWORD = (By.XPATH, "//div[label[contains(text(),'Пароль')]]//input") # Поле ввода пароля

    # Вход
    LOGIN_FORM_BUTTON = (By.XPATH, "//button[text()='Войти']") # Кнопка входа в форме авторизации

    # Выход
    LOGOUT_BUTTON = ("xpath", "//button[text()='Выход']") # Кнопка выхода в личном кабинете

    # Конструктор
    CONSTRUCTOR_BUTTON = ("xpath", "//header//a[contains(@class, 'AppHeader_header__link') and @href='/']")
    BULKI = ("xpath", "//span[text()='Булки']") # Вкладка "Булки"
    SOUS = ("xpath", "//span[text()='Соусы']") # Вкладка «Соусы»
    NACHINKI = ("xpath", "//span[text()='Начинки']") # Вкладка «Начинки»

    LOGIN_BUTTON_REG_FORM = ("xpath", "//a[contains(@class, 'Auth_link__1fOlj') and text()='Войти']")
    RESTORE_PASSWORD_BUTTON = ("xpath", "//a[text()='Восстановить пароль']") # Кнопка Восстановить пароль
    LOGIN_BUTTON_RESTORE_FORM = ("xpath", "//a[@href='/login' and text()='Войти']") # Кнопка входа на странице восстановления пароля
    INVALID_PASSWORD_ERROR = ("xpath", "//p[contains(text(), 'Некорректный пароль')]") # Ошибка при некорректном пароле