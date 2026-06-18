from InstaFollower import InstaFollower

insta_follower = InstaFollower() # Create an instance of the InstaFollower class
insta_follower.retry(insta_follower.login(), description="Login") # Retry the login function
insta_follower.retry(insta_follower.find_followers(), description="Find Followers") # Retry the find_followers function
insta_follower.retry(insta_follower.follow(), description="Follow") # Retry the follow function