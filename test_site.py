from selenium import webdriver

import pytest
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser():
    browser = webdriver.Yandex()
    browser.maximize_window()
    yield browser

def test_open_s6(browser):
    browser.get('https://demoblaze.com/index.html')
    galaxy_s6 = browser.find_element(By.LINK_TEXT, value: 'Samsung galaxy s6')
    galaxy_s6.click()
    title = browser.find_element(By.CSS_SELECTOR, value: 'h2')

    assert title.text == 'Samsung galaxy s6'