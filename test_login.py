from playwright.sync_api import Page, expect
import pytest

# def test_login(page: Page):
#     page.goto('https://saucedemo.com')

#     page.locator('[data-test="username"]').fill('standard_user')
#     page.locator('[data-test="password"]').fill('secret_sauce')
#     page.locator('[data-test="login-button"]').click()

#     expect(page).to_have_url('https://www.saucedemo.com/inventory.html')
#     expect(page).to_have_title('Swag Labs')

#     inventory_page_title = page.locator('//div[@class="app_logo"]').text_content()

#     assert inventory_page_title == 'Swag Labs'

#     page.pause()

test = [('standard_user', 'secret_sauce'),]

@pytest.mark.parametrize('username, password', test)
def test_login_positive(page: Page, username, password):
    page.goto('https://saucedemo.com')

    page.locator('[data-test="username"]').fill(username)
    page.locator('[data-test="password"]').fill(password)
    page.locator('[data-test="login-button"]').click()

    inventory_page_title = page.locator('//div[@class="app_logo"]').text_content()

    assert inventory_page_title == 'Swag Labs'