import os
from behave import given, when, then
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
login_page_url = os.getenv("LOGIN_PAGE_URL")

@given('the user is on the login page')
def user_is_on_login_page(context):
    # Crear opciones para el controlador Chrome
    chrome_options = Options()
    # Opcionalmente, puedes configurar las opciones aquí, como:
    # chrome_options.add_argument('--headless')

    # Inicializar el controlador de Chrome con las opciones
    context.custom_context.driver = webdriver.Chrome(options=chrome_options)
    context.custom_context.driver.get(login_page_url)

@when('the user enters valid credentials')
def user_enters_valid_credentials(context):
    # Implement code to enter valid credentials
    pass

@then('the user should be logged in successfully')
def user_logged_in_successfully(context):
    # Implement verification code for successful login
    pass

# Implement steps for other scenarios in login.feature
