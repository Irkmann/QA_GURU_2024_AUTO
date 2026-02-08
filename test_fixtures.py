import pytest


@pytest.fixture
def login_page(browser):
    print("Логин пейдж!")# Пишем фикстуру для страницы авторизации
    pass


@pytest.fixture
def user():
    print("Юзер!")# Пишем фикстуру для получения пользовательских данных
    return "username", "password"

def test_login(login_page, user): # Пишем функцию теста
    username, password = user
    assert username == "username"
    assert password == "password"

def test_logout(login_page, user): # Пишем функцию теста
    username, password = user
    assert username == "username"
    assert password == "password"

