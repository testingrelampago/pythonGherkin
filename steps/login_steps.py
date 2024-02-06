from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
login_page_url = os.getenv("LOGIN_PAGE_URL")


@given('the user is on the login page')
def user_is_on_login_page(context):
    # Specify the ChromeDriver version
    context.driver = webdriver.Chrome(ChromeDriverManager().install())

    # Navigate to the login page URL
    context.driver.get(login_page_url)

@when('the user enters valid credentials')
def user_enters_valid_credentials(context):
    # Implement code to enter valid credentials
    pass

@then('the user should be logged in successfully')
def user_logged_in_successfully(context):
    # Implement verification code for successful login
    pass

# Implement steps for other scenarios in login.feature
