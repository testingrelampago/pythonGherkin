from behave import fixture, use_fixture
from selenium import webdriver
from context import CustomContext

@fixture
def browser_chrome(context):
    context.custom_context.driver = webdriver.Chrome()
    yield context.custom_context.driver
    context.custom_context.driver.quit()

def before_feature(context, feature):
    # Any setup code before each feature
    context.custom_context = CustomContext()
    context.config.setup_logging()
    context.config.browser_chrome = browser_chrome

def after_all(context):
    # Any cleanup code after all scenarios
    if hasattr(context.custom_context, 'driver'):
        context.custom_context.driver.quit()
