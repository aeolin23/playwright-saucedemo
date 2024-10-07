from playwright.sync_api import Page, expect
import pytest

# positive login test case
data_login = [('standard_user', 'secret_sauce'),]

@pytest.mark.parametrize('username, password', data_login)
def test_login_positive(page: Page, username, password):
    page.goto('https://saucedemo.com')

    page.locator('[data-test="username"]').fill(username)
    page.locator('[data-test="password"]').fill(password)
    page.locator('[data-test="login-button"]').click()

    inventory_page_title = page.locator('//div[@class="app_logo"]').text_content()

    assert inventory_page_title == 'Swag Labs'

# negative login test case
data_login_negative = [('standard_user','','Epic sadface: Password is required'),
                    ('','secret_sauce','Epic sadface: Username is required'),
                    ('locked_out_user','secret_sauce','Epic sadface: Sorry, this user has been locked out.'),]

@pytest.mark.parametrize('username, password, error', data_login_negative)
def test_login_negative(page: Page, username, password, error):
    page.goto('https://saucedemo.com')

    page.locator('//*[@id="user-name"]').fill(username)
    page.locator('[data-test="password"]').fill(password)
    page.locator('[id="login-button"]').click()

    error_text = page.locator('[data-test="error"]').inner_text()

    assert error_text == error

# checkout test case
data_checkout = [('standard_user', 'secret_sauce', 'Ludwig', 'Wahlberg', '54321'),]

@pytest.mark.parametrize('username, password, first_name, last_name, postal_code', data_checkout)
def test_checkout(page: Page, username, password, first_name, last_name, postal_code):
    page.goto('https://saucedemo.com')

    page.locator('[data-test="username"]').fill(username)
    page.locator('[data-test="password"]').fill(password)
    page.locator('[data-test="login-button"]').click()

    inventory_page_title = page.locator('//div[@class="app_logo"]').text_content()

    assert inventory_page_title == 'Swag Labs'

    page.locator('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-fleece-jacket"]').click()

    qty = page.locator('[data-test="shopping-cart-badge"]').inner_text()

    assert qty == '2'

    page.locator('[data-test="shopping-cart-link"]').click()

    cart_title = page.locator('[data-test="title"]').inner_text()

    assert cart_title == 'Your Cart'

    page.locator('[data-test="checkout"]').click()

    checkout_step_one_title = page.locator('[data-test="title"]').inner_text()

    assert checkout_step_one_title == 'Checkout: Your Information'

    page.locator('[data-test="firstName"]').fill(first_name)
    page.locator('[data-test="lastName"]').fill(last_name)
    page.locator('[data-test="postalCode"]').fill(postal_code)
    page.locator('[data-test="continue"]').click()

    checkout_step_two_title = page.locator('[data-test="title"]').inner_text()

    assert checkout_step_two_title == 'Checkout: Overview'

    page.locator('[data-test="finish"]').click()

    checkout_complete = page.locator('[data-test="title"]').inner_text()

    assert checkout_complete == 'Checkout: Complete!'

    page.locator('[data-test="back-to-products"]').click()

    inventory_page_title = page.locator('//div[@class="app_logo"]').text_content()

    assert inventory_page_title == 'Swag Labs'

# logout test case
@pytest.mark.parametrize('username, password', data_login)
def test_login_positive(page: Page, username, password):
    page.goto('https://saucedemo.com')

    page.locator('[data-test="username"]').fill(username)
    page.locator('[data-test="password"]').fill(password)
    page.locator('[data-test="login-button"]').click()

    inventory_page_title = page.locator('//div[@class="app_logo"]').text_content()

    assert inventory_page_title == 'Swag Labs'

    burger_menu = page.locator('//button[@id="react-burger-menu-btn"]').click()

    page.locator('[data-test="logout-sidebar-link"]').click()

    login_btn = page.locator('[data-test="login-button"]').input_value()

    assert login_btn == 'Login'