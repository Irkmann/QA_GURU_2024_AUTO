import pytest
from selene import browser, be, have
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_success_search(setup_chrome):
    search_query = "Selenium Python"

    # 1. Находим поле поиска
    search_input = browser.element('[class="search3__input mini-suggest__input"]')
    search_input.should(be.visible)
    search_input.should(be.enabled)
    search_input.should(be.clickable)

    # 2. Вводим значение
    search_input.type(search_query)

    # 3. Нажимаем Enter для поиска
    search_input.press_enter()

    browser.element('#search').should(be.visible)

#def test_fail_search(setup_chrome):
    #pass

