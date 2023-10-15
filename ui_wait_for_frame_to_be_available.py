from pickle import FRAME
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

def test_wait_for_frame_to_be_available(page):
    page.goto("https://play1.automationcamp.ir/expected_conditions.html")
    click_trigger_btn = page.locator("#wait_for_frame")
    click_trigger_btn.click()
    
    #page.wait_for_selector("#frm")????

#frame = page.frame_locator("iframe#frm").locator("#inner_button").click()
    frame_element = page.frame_locator("iframe#frm")
    inner_button = frame_element.locator("#inner_button")
    
    inner_button.click()

#result_inner_btn_locator = page.locator("#inner_button")
#result_inner_btn_locator.click()
    assert inner_button.inner_text() == 'Clicked'


