import pytest
from locators import Locators


class TestConstructor:
    def test_constructor_bulki(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*Locators.SOUS).click()
        driver.find_element(*Locators.BULKI).click()

        bulki_visible = driver.find_element(*Locators.BULKI).text
        assert bulki_visible == "Булки"


    def test_constructor_sous(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*Locators.SOUS).click()

        sous_visible = driver.find_element(*Locators.SOUS).text
        assert sous_visible == "Соусы"

    def test_constructor_nachinky(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(*Locators.NACHINKI).click()

        nachinky_visible = driver.find_element(*Locators.NACHINKI).text
        assert nachinky_visible == "Начинки"