import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class BasePage:
    def __init__(self, page):
        self.page = page
        self.base_url = os.getenv("BASE_URL")
        self.dashboard_path = "/loads?filter=mine&page=1"

    def navigate(self):
        self.page.goto(self.base_url)
