import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import *
from locators import Locators
from data import Credentials

class TestEntranceAccount():
    # вход по кнопке Войти в аккаунт на главной странице
    def test_entrance_button_on_main_site(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_FORM_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site


    def test_entrance_button_personal_account(self, driver):
        # вход через кнопку «Личный кабинет»
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_FORM_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site


    def test_entrance_button_registration(self, driver):
        # вход через кнопку в форме регистрации
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.LOGIN_BUTTON_REG_FORM).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_FORM_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site


    def test_entrance_forget_password(self, driver):
        # вход через кнопку в форме восстановления пароля
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*Locators.RESTORE_PASSWORD_BUTTON).click()
        driver.find_element(*Locators.LOGIN_BUTTON_RESTORE_FORM).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_FORM_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site