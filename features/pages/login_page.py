from playwright.sync_api import expect
from utilities.utilities import set_test_status
from pages.base_page import BasePage

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class LoginPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.username_input_locator = page.locator("#username")
        self.password_input_locator =  page.locator("#password")
        self.continue_button_locator = page.locator('button[type="submit"]').first
                    
    def fill_username(self, username):
        if username == 'MASKED':
            username = os.getenv("DEEPPACK_USERNAME")
        self.username_input_locator.fill(username)   

    def fill_password(self, password):
        if password == 'MASKED':
            password = os.getenv("DEEPPACK_PASSWORD")
        self.password_input_locator.fill(password)   
      

    def click_on(self):
        self.continue_button_locator.click()           

    def assert_login(self):
        (self.page).wait_for_url(f"{self.base_url}{self.dashboard_path}")
        expect(self.page).to_have_url(f"{self.base_url}{self.dashboard_path}")  