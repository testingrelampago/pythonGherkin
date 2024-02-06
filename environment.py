from behave import fixture
from selenium import webdriver
from context import CustomContext

def before_all(context):
    # Inicializar el objeto CustomContext
    context.custom_context = CustomContext()

@fixture
def browser_chrome(context):
    # Inicializar el controlador de Chrome
    context.custom_context.driver = webdriver.Chrome()
    yield context.custom_context.driver
    # Cerrar el controlador de Chrome después de usarlo
    context.custom_context.driver.quit()

def before_feature(context, feature):
    # Configurar el fixture para el navegador Chrome
    context.config.browser_chrome = browser_chrome

def after_all(context):
    # Limpiar el contexto después de ejecutar todas las pruebas
    if hasattr(context, 'custom_context') and context.custom_context.driver:
        context.custom_context.driver.quit()
