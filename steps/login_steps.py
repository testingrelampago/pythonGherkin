# -----

#
# Feature: User login functionality
#

# -----

import os
from selenium import webdriver
from dotenv import load_dotenv
from behave import given, when, then
from selenium.webdriver.chrome.options import Options

# Add variable in .env
load_dotenv()
login_page_url = os.getenv("LOGIN_PAGE_URL")

# -----

# Scenario: Successful login

# -----

@given('the user is on the login page')
def user_is_on_login_page(context):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # Comment the last line if you want to see Chrome driver

    context.custom_context.driver = webdriver.Chrome(options=chrome_options)
    context.custom_context.driver.get(login_page_url)

@when('the user enters valid credentials')
def user_enters_valid_credentials(context):
    # Implement code
    pass

@then('the user should be logged in successfully')
def user_logged_in_successfully(context):
    # Implement code
    pass

# -----

# Scenario: Invalid login attempt

# -----

@when('the user enters invalid credentials')
def user_enters_invalid_credentials(context):
    # Implement code
    pass

@then('an error message should be displayed')
def user_see_an_error_displayed(context):
    # Implement code
    pass