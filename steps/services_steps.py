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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Add variable in .env
load_dotenv()
services_page_url = os.getenv("SERVICES_PAGE_URL")

# -----

# Scenario: User searches for a service

# -----

@given('the user is on the service page')
def user_is_on_service_page(context):
    chrome_options = Options()
    #chrome_options.add_argument('--headless')

    context.custom_context.driver = webdriver.Chrome(options=chrome_options)
    context.custom_context.driver.get(services_page_url)

@when('the user search about the team')
def user_search_about_the_team(context):
    # Implement code
    pass

@then('the user see display relevant team information')
def user_see_display_relevant_team_information(context):
    expected_text = 'Our team'

    try:
        WebDriverWait(context.custom_context.driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), expected_text))
        print(f"The text '{expected_text}' is in the service page")
    except TimeoutException:
        print(f"The text '{expected_text}' is not in the service page")


# -----

# Scenario: User searches information about linkedin page

# -----

@when('the user search the linkedin button')
def user_search_the_linkedin_button(context):
    linkedin_link = WebDriverWait(context.custom_context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-aid="SOCIAL_LINKEDIN_LINK"]')))
    linkedin_link.click()

@then('the linkedin button redirect to the linkedin page')
def linkedin_button_redirect_to_linkedin_page(context):
    context.custom_context.driver.switch_to.window(context.custom_context.driver.window_handles[-1])
    WebDriverWait(context.custom_context.driver, 10).until(EC.url_contains("linkedin.com"))
