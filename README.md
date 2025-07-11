# SnapBuy QA Portfolio

This repository contains my complete **Selenium automation scripts, manual testing, and Jira sprint tracking** for the **SnapBuy E-commerce Project**.


##  Selenium Automation Script

**`/tests/selenium/snapbuy_login_test.py`**

This is a **basic Selenium Python script** that automates the SnapBuy user login flow:

- Opens the live SnapBuy login page hosted on Render.com
- Handles **cold start delay** using `WebDriverWait`
- Fills valid username & password automatically
- Clicks **Login**
- Verifies redirect to the **Dashboard**
- Prints ✅ if successful, ❌ if failed

**How to run:**
1. Install Selenium:
   ```bash
   pip install selenium

  Download ChromeDriver matching your Chrome version.
  Place chromedriver.exe in /tests/selenium/ (this file is ignored in .gitignore).

Run:
    cd tests/selenium
    python snapbuy_login_test.py


# SnapBuy QA Test Cases

This repository contains my end-to-end QA work for the **SnapBuy E-commerce Project**.

##  Manual Test Cases
-  [SnapBuy_Manual_Test_Cases.pdf](SnapBuy_Manual_Test_Cases.pdf)

Includes test scenarios for:
- User Registration & Email Verification
- User Login
- Cart Operations
- Payment Checkout & Razorpay Integration

##  Jira Sprint Report Proof
-  [SnapBuy_Jira_Sprint1_Completed.png]

I planned and executed a full QA sprint using **Jira Scrum**, moving all test cases through:
`To Do → In Progress → Done`.

##  Tools Used
- Manual Testing
- Jira for test tracking & sprint management
- Postman for API validation 
