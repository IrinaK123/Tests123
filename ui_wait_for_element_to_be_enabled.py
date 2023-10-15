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

def test_wait_for_element_to_be_enabled(page):
    page.goto("https://play1.automationcamp.ir/expected_conditions.html")
    click_trigger_btn = page.locator("#enabled_trigger")
    click_trigger_btn.click()
    
    page.wait_for_selector("#enabled_target")
    
    result_btn_locator = page.locator("#enabled_target")
    result_btn_locator.click()
    
    page.wait_for_selector("div.popover:visible")
    
    header_text = page.locator("h3.popover-header").inner_text()
    body_text = page.locator("div.popover-body").inner_text()
    
    assert header_text == "Yay! I am super active now!"
    assert body_text == "See, you just clicked me!!"
    assert result_btn_locator.inner_text() == 'Enabled Button'




