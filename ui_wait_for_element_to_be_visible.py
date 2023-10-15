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

def test_wait_for_element_to_be_visible(page):
    page.goto("https://play1.automationcamp.ir/expected_conditions.html")
    click_show_alert_btn = page.locator("#visibility_trigger")
    click_show_alert_btn.click()
    
    
    
    result_btn_locator = page.locator("#visibility_target")
    result_btn_locator.click()
    
    page.wait_for_selector("div.popover:visible")
    
    header_text = page.locator("h3.popover-header").inner_text()
    body_text = page.locator("div.popover-body").inner_text()
    
    assert header_text == "Can you see me?"
    assert body_text == "I just removed my invisibility cloak!!"
    assert result_btn_locator.inner_text() == 'Click Me'


