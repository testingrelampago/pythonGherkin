import os
from behave import given, when, then
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
search_page_url = os.getenv("LOGIN_PAGE_URL")

@given('the user is on the search page')
def user_is_on_search_page(context):
    # Crear opciones para el controlador Chrome
    chrome_options = Options()
    # Opcionalmente, puedes configurar las opciones aquí, como:
    # chrome_options.add_argument('--headless')

    # Inicializar el controlador de Chrome con las opciones
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

# Implement steps for other scenarios in search.feature
