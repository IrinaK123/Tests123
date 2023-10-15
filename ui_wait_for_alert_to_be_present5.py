import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='function')
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()
        yield page
        page.close()
        browser.close()

def test_wait_for_alert_to_be_present(page):
    page.goto("https://play1.automationcamp.ir/expected_conditions.html")
    click_show_alert_btn = page.locator("text=Show Alert")
    click_show_alert_btn.click()
    
    page.wait_for_selector("#alert_handled_badge") 
    
    result_msg_locator = page.locator("#alert_handled_badge")
    
    assert result_msg_locator.inner_text() == 'Alert handled'


