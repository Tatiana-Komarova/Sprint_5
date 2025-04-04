import pytest
from locators import Locators


class TestConstructor:
    def test_constructor_bulki(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*Locators.SOUS).click()
        driver.find_element(*Locators.BULKI).click()

        active_tab = driver.find_element(*Locators.ACTIVE_TAB).text
        assert active_tab == "Булки"


    def test_constructor_sous(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*Locators.SOUS).click()

        active_tab = driver.find_element(*Locators.ACTIVE_TAB).text
        assert active_tab == "Соусы"

    def test_constructor_nachinky(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*Locators.NACHINKI).click()

        active_tab = driver.find_element(*Locators.ACTIVE_TAB).text
        assert active_tab == "Начинки"
