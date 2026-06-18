import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

load_dotenv()

BASE_URL = os.getenv("BASE_URL") # URL to share a naan
EMAIL = os.getenv("SHARE_A_NAAN_EMAIL") # Email to share a naan
PASSWORD = os.getenv("SHARE_A_NAAN_PASSWORD") # Password to share a naan
SIMULAR_ACCOUNT = os.getenv("SIMULAR_ACCOUNT") # The account whose followers you will follow

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
        self.driver.get(BASE_URL)  # go to the website
        wait = WebDriverWait(self.driver, 5)  # Create a new wait object

        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/aside/div/form/input[1]")))  # Wait for the email input field to appear
        email_input.clear()  # Clear the email input field
        email_input.send_keys(EMAIL)  # Enter the email address from the .env file

        password_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/aside/div/form/input[2]")))  # Wait for the password input field to appear
        password_input.clear()  # Clear the password input field
        password_input.send_keys(PASSWORD)  # Enter the password from the .env file

        submit_btn = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/aside/div/form/button")))  # Wait for the Submit button to appear
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
        :return: followers
        """
        pass
    def follow(self):
        """
        Follow the followers
        :return:
        """
        pass
    def retry(func, retries=7, description=None):
        """
        Retry a function if it fails
        :param func: a function to retry
        :param retries: retry count
        :param description: description of the function
        :return: function result
        """
        for attempt in range(1, retries + 1):  # Retry up to retries times
            try:  # Try to execute the function
                print(f"Attempt {attempt}/{retries} → {description}")  # Print the attempt number
                return func()  # Return the function result

            except (TimeoutException, NoSuchElementException, ElementClickInterceptedException, Exception) as e:
                print(f"Failed attempt {attempt}: {e}")  # Print the failure message
                time.sleep(1)  # Wait for 1 second before retrying

        raise Exception(f"❌ All retries failed for: {description}")  # If all retries fail, raise an exception