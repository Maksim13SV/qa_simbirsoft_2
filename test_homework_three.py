import pytest
from selene import browser, have

@pytest.fixture()
def open_browser():
    browser.open('https://duckduckgo.com/')

# Позитивный кейс
def test_duckduckgo_search_positive(open_browser):
    browser.element('input[type="text"]').type('Simbirsoft').press_enter()
    browser.element('//span[contains(text(),"Разработка программного обеспечения на заказ")]') \
        .should(have.text('Разработка программного обеспечения на заказ - SimbirSoft'))

# Негативный кейс
def test_duckduckgo_search_negative(open_browser):
    browser.element('input[name="q"]').type('ajshdjakshd1231321').press_enter()
    browser.element('#links').should(have.no.text('ajshdjakshd1231321'))