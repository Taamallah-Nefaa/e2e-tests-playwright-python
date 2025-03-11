from playwright.sync_api import sync_playwright
from pages.base_page import BasePage
from pages.login_page import LoginPage
import os
from dotenv import load_dotenv
from datetime import datetime


# Load environment variables from .env file
load_dotenv()


def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=eval(os.getenv("IS_HEADLESS")))
    
def after_all(context):
    context.browser.close()
    context.playwright.stop()

def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.base_page = BasePage(context.page)
    context.login_page = LoginPage(context.page)
    
    context.base_page.navigate()

def after_scenario(context, scenario):
    if scenario.status == "failed":
        take_screenshot(context, scenario)
    context.page.close()



def take_screenshot(context, scenario):
    # Create a directory for screenshots if it doesn't exist
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
        
    # Generate a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join(screenshots_dir, f"{scenario.name}_{timestamp}.png")
        
    # Take the screenshot
    context.page.screenshot(path=screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")