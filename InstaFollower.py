import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

load_dotenv()

BASE_URL = os.getenv("BASE_URL") # URL to share a naan
EMAIL = os.getenv("SHARE_A_NAAN_EMAIL") # Email to share a naan
PASSWORD = os.getenv("SHARE_A_NAAN_PASSWORD") # Password to share a naan
SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT") # The account whose followers you will follow

class InstaFollower:
    def __init__(self):
        """
        Initialize the bot
        """
        chrome_options = webdriver.ChromeOptions()  # Create a new option object
        chrome_options.add_experimental_option("detach", True)  # Attach the driver to the background

        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")  # Set the user data directory
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")  # Add the user data directory argument

        self.driver = webdriver.Chrome(options=chrome_options)  # Set up Selenium

    def login(self):
        """
        Login to the share-a-naan website
        """
        self.driver.get(f"{BASE_URL}/login")  # go to the website
        wait = WebDriverWait(self.driver, 5)  # Create a new wait object

        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/form/input[1]")))  # Wait for the email input field to appear
        email_input.clear()  # Clear the email input field
        email_input.send_keys(EMAIL)  # Enter the email address from the .env file

        password_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/form/input[2]")))  # Wait for the password input field to appear
        password_input.clear()  # Clear the password input field
        password_input.send_keys(PASSWORD)  # Enter the password from the .env file

        submit_btn = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/form/button")))  # Wait for the Submit button to appear
        submit_btn.click()  # Click the Submit button

        try:  # If the Not Now button doesn't appear, continue
            not_now_save_info_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[2]')))  # Find the not now button
            not_now_save_info_btn.click()  # Click the not now button
            print("Not Now button clicked")
        except:  # If the Not Now button doesn't appear, continue
            print("Not Now button didn't appear, continuing...")

        try:  # If the Not Now button doesn't appear, continue
            not_now_turn_on_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/button[2]')))  # Find the not now button
            not_now_turn_on_btn.click()  # Click the not now button
            print("Not Now button clicked")
        except:  # If the Not Now button doesn't appear, continue
            print("Not Now button didn't appear, continuing...")

        return "OK"
    def find_followers(self):
        """
        Find the followers of the account whose followers you will follow
        """
        self.driver.get(f"{BASE_URL}/u/{SIMILAR_ACCOUNT}/followers") # go to the followers page
        wait = WebDriverWait(self.driver, 5)  # Create a new wait object

        try: # Try to find the modal
            modal = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[3]'))) # Find the modal
            print("Find the followers list")

            for _ in range(10): # Load the followers list 10 times
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal) # Scroll to the bottom of the modal
                time.sleep(1) # Wait for 1 second
        except:  # If the modal doesn't appear, continue
            print("Modal didn't appear, continuing...")
    def follow(self):
        """
        Follow the followers
        :return:
        """
        pass