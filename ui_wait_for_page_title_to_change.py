import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='function')
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=3000)
        page = browser.new_page()
        yield page
        page.close()
        browser.close()

def test_wait_for_page_title_to_change(page):
    page.goto("https://play1.automationcamp.ir/expected_conditions.html")
    
    trigger_btn = page.locator("#page_title_trigger")
    trigger_btn.click()
    
   
    current_title = page.title()
    
    new_title = page.title()
    
    assert new_title == "My New Title!"

if __name__ == "__main__":
    pytest.main(["-k", "test_page_title_change_after_click"])






