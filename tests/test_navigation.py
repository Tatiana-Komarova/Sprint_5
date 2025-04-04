import pytest
from curl import *
from locators import Locators
from data import Credentials
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPersonalAccount:
    # проверка перехода по клику на "Личный кабинет"
    def test_click_shift_on_personal_account(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_FORM_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(profile))

        assert driver.current_url == profile

    # переход из Личного кабинета в Конструктор
    def test_from_personal_account_to_constructor(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_FORM_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        driver.find_element(*Locators.CONSTRUCTOR_BUTTON ).click()

        assert driver.current_url == main_site

    # переход из Личного кабинета на Логотип
    def test_from_personal_account_to_logo(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_FORM_BUTTON).click()

        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        driver.find_element(*Locators.LOGO).click()

        assert driver.current_url == main_site