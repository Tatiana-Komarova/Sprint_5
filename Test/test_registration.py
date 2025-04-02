import pytest
from curl import *
from locators import Locators
from Test.helper import generate_registration_data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistrationWithNewCredentials():
    #регистрация нового пользователя
    def test_sucsess_registration(self, driver):
        email, password, name = generate_registration_data()
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(URL))

        assert driver.current_url == URL

    # регистрация с некорректным паролем
    def test_with_invalid_password_registration(self, driver):
        email, name, password = generate_registration_data()
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys('123')
        driver.find_element(*Locators.REG_BUTTON).click()
        reg_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.INVALID_PASSWORD_ERROR)).text

        assert reg_text == 'Некорректный пароль'