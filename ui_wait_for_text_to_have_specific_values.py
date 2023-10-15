import re
from playwright.sync_api import expect
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='function')
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        yield page
        page.close()
        browser.close()

def test_wait_for_text_to_have_specific_values(page):
    page.goto("https://play1.automationcamp.ir/expected_conditions.html")
    click_trigger_btn = page.locator("#text_value_trigger")
    click_trigger_btn.click()
    #page.wait_for_timeout(10000)
    #new_value_locator = page.get_by_text("Dennis Ritchie")
    #new_value_locator = page.wait_for_selector('text=Dennis Ritchie')
    #new_value_locator.wait_for(has_text="Dennis Ritchie")

    page.wait_for_selector("#wait_for_text")
    
    new_value_locator = page.get_by_placeholder("Creator of C")
    
    #assert new_value_locator.inner_text() == 'Dennis Ritchie'
    #expect(new_value_locator).to_have_text("Dennis Ritchie")
    expect(new_value_locator).to_have_value("Dennis Ritchie")


