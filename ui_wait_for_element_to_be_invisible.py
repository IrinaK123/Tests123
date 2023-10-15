import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        yield browser
        browser.close()

def test_locate_and_click_button(browser):
    page = browser.new_page()
    page.goto("https://play1.automationcamp.ir/expected_conditions.html")  

    trigger_button = page.locator("button#invisibility_trigger")
    trigger_button.click()
    
    page.wait_for_selector("#spinner_gone")  
    
    assert page.get_by_text("Thank God that spinner is gone!").is_visible()

    browser.close()

