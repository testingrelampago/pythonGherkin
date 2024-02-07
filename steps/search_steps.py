# -----

#
# Feature: Search information in service page
#

# -----

import os
from selenium import webdriver
from dotenv import load_dotenv
from behave import given, when, then
from selenium.webdriver.chrome.options import Options

# Add variable in .env
load_dotenv()
search_page_url = os.getenv("LOGIN_PAGE_URL")

# -----

# Scenario: User searches for a service

# -----

@given('the user is on the service page')
def user_is_on_service_page(context):
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    context.custom_context.driver = webdriver.Chrome(options=chrome_options)
    context.custom_context.driver.get(search_page_url)

@when('the user search about the team')
def user_search_about_the_team(context):
    # Implement code to enter a product name
    pass

@then('the user see display relevant team information')
def user_see_display_relevant_team_information(context):
    # Implement verification code for relevant search results
    pass

# -----

# Scenario: User searches information about linkedin page

# -----

@when('the user search the linkedin button')
def user_search_the_linkedin_button(context):
    # Implement code to enter a product name
    pass

@then('the linkedin button redirect to the linkedin page')
def linkedin_button_redirect_to_linkedin_page(context):
    # Implement verification code for relevant search results
    pass