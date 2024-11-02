from playwright.sync_api import Page, expect
import pytest
from pages.login import LoginPage
from pages.inventory import InventoryPage

@pytest.fixture
def browser(page: Page):
    page.set_viewport_size({'width': 1920, 'height': 1080})
    yield page
    page.close()

# positive login
def test_login_positive(browser):
    login = LoginPage(browser)
    inventory = InventoryPage(browser)

    browser.goto('https://saucedemo.com')

    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login_button()

    expect(browser).to_have_title('Swag Labs')
    expect(browser).to_have_url("https://www.saucedemo.com/inventory.html")

    inventory_page_title = inventory.check_page_title()
    assert inventory_page_title == 'Swag Labs'

# negative login
data_login_negative = [('standard_user','','Epic sadface: Password is required'),
                    ('','secret_sauce','Epic sadface: Username is required'),
                    ('locked_out_user','secret_sauce','Epic sadface: Sorry, this user has been locked out.'),]

@pytest.mark.parametrize('username, password, error', data_login_negative)
def test_login_negative(browser, username, password, error):
    login = LoginPage(browser)

    browser.goto('https://saucedemo.com')

    login.input_username(username)
    login.input_password(password)
    login.click_login_button()
    error_text = login.error_message()

    assert error_text == error