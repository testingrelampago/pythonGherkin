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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    username_input = context.custom_context.driver.find_element(By.ID, 'username')  # Cambia el selector según tu página de inicio de sesión
    password_input = context.custom_context.driver.find_element(By.ID, 'password')  # Cambia el selector según tu página de inicio de sesión
    login_button = context.custom_context.driver.find_element(By.ID, 'login-button')  # Cambia el selector según tu página de inicio de sesión

    username_input.send_keys('tu_usuario')  # Reemplaza 'tu_usuario' por el nombre de usuario real
    password_input.send_keys('tu_contraseña')  # Reemplaza 'tu_contraseña' por la contraseña real
    login_button.click()

    # Espera a que la página cargue después del inicio de sesión (ejemplo: espera a que aparezca un elemento en la página de inicio)
    WebDriverWait(context.custom_context.driver, 10).until(EC.presence_of_element_located((By.ID, 'dashboard')))  # Cambia el selector según la página de destino después del inicio de sesión


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