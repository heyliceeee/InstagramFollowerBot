import time
from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from InstaFollower import InstaFollower

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

insta_follower = InstaFollower() # Create an instance of the InstaFollower class
retry(insta_follower.login, description="Login") # Retry the login function
retry(insta_follower.find_followers, description="Find Followers") # Retry the find_followers function
retry(insta_follower.follow, description="Follow") # Retry the follow function