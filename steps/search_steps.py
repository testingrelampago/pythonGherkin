# -----

#
# Feature: Search functionality
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

# Scenario: User searches for a product

# -----

@given('the user is on the search page')
def user_is_on_search_page(context):
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    context.custom_context.driver = webdriver.Chrome(options=chrome_options)
    context.custom_context.driver.get(search_page_url)

@when('the user enters a product name')
def user_enters_product_name(context):
    # Implement code to enter a product name
    pass

@then('the search results should display relevant products')
def search_results_display_relevant_products(context):
    # Implement verification code for relevant search results
    pass

# -----

# Scenario: User searches with an empty query

# -----

@when('the user submits an empty search')
def user_submits_empty_search(context):
    # Implement code to enter a product name
    pass

@then('a message should indicate no results')
def message_should_indicate_no_results(context):
    # Implement verification code for relevant search results
    pass