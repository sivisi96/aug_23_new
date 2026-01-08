from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# Фикстура для инициализации и завершения работы браузера
@pytest.fixture()
def browser():
    # Используйте браузер Chrome
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()

# Тест открывания страницы с товаром Samsung Galaxy S6
def test_open_s6(browser):
    browser.get('https://demoblaze.com/index.html')
    # Поиск элемента по ссылке с текстом "Samsung galaxy s6"
    galaxy_s6 = browser.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
    galaxy_s6.click()
    # Получение заголовка страницы
    title = browser.find_element(By.CSS_SELECTOR, 'h2').text
    # Проверка соответствия названия товара
    assert title == 'Samsung galaxy s6'