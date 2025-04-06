import pytest
from curl import *
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials

class TestExit:
    def test_exit_from_account(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_FORM_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(URL))

        assert driver.current_url == URL