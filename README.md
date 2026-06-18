# **InstaFollower Bot**

Automated Selenium bot that logs into the *Share‑a‑Naan* platform, loads the followers of a target account, and follows them automatically.  
Includes a retry mechanism to handle temporary UI failures, slow loading, or intercepted clicks.

---

## **Features**
- Logs into the platform using stored credentials  
- Opens the followers list of a specified account  
- Scrolls the modal to load more followers  
- Clicks all available **Follow** buttons  
- Handles “Unfollow?” pop‑ups automatically  
- Retries unstable actions (timeouts, missing elements, intercepted clicks)

---

## **Environment Variables**
Create a `.env` file with:

```
BASE_URL=https://example.com
SHARE_A_NAAN_EMAIL=your_email
SHARE_A_NAAN_PASSWORD=your_password
SIMILAR_ACCOUNT=username_to_scrape
```

---

## **Installation**
```bash
pip install selenium python-dotenv
```

Download the appropriate ChromeDriver version for your browser.

---

## **How It Works**
### **1. Login**
The bot navigates to the login page, fills in credentials, submits the form, and dismisses optional pop‑ups.

### **2. Load Followers**
It opens the followers modal of the target account and scrolls it multiple times to load more entries.

### **3. Follow Users**
It clicks each **Follow** button.  
If a click triggers an “Unfollow?” dialog, the bot selects **Cancel** and continues.

### **4. Retry Wrapper**
A simple retry function wraps each main action:

- Executes the function  
- If it fails due to Selenium exceptions, retries up to 7 times  
- Raises an error only after all attempts fail  

---

## **Usage**
```python
from InstaFollower import InstaFollower
from retry import retry   # if stored separately

insta = InstaFollower()

retry(insta.login, description="Login")
retry(insta.find_followers, description="Load Followers")
retry(insta.follow, description="Follow Users")
```

---

## **Project Structure**
```
.
├── InstaFollower.py
├── main.py
├── .env
└── chrome_profile/
```

---

## **Notes**
- The bot uses a persistent Chrome profile to reduce repeated logins.  
- XPaths may need updates if the website UI changes.  
- Use responsibly — automated following may violate platform rules.