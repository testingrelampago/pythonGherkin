from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@given('the user is on the search page')
def user_is_on_search_page(context):
    # Assuming you are using Chrome WebDriver, you can change it to other WebDriver if needed
    context.custom_context.driver = webdriver.Chrome(ChromeDriverManager().install())

    # Navigate to the search page URL
    search_page_url = 'https://www.testingrelampago.com/search'
    context.custom_context.driver.get(search_page_url)

@when('the user enters a product name')
def user_enters_product_name(context):
    # Implement code to enter a product name
    pass

@then('the search results should display relevant products')
def search_results_display_relevant_products(context):
    # Implement verification code for relevant search results
    pass

# Implement steps for other scenarios in search.feature