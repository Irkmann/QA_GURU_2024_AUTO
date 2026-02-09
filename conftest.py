import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def setup_chrome():
    # Настройка Chrome с размером 400x400
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1000,1000")

    driver = webdriver.Chrome(options=chrome_options)
    browser.config.driver = driver
    browser.config.timeout = 10

    # Открываем Google
    browser.open("https://ya.ru/")

    yield browser

    browser.quit()