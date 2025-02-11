from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.text_box_page import TextBoxPage

@given('the user is on the Text Box page')
def step_impl(context):
    context.text_box_page = TextBoxPage(context.driver)
    context.text_box_page.open()

@when('the user fills in the form with valid data')
def step_impl(context):
    context.text_box_page.fill_form(
        'Camila Alejandra Suarez Urrego',
        'alejandra.urrego@outlook.com',
        'Ac 57 r sur #66',
        'Ac 57 r sur #66'
    )
    context.text_box_page.submit_form()

@then('the user should see the correct submitted values')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'border'))
    )

    name, email, current_address, permanent_address = context.text_box_page.get_output()

    assert 'Camila Alejandra Suarez Urrego' in name
    assert 'alejandra.urrego@outlook.com' in email
    assert 'Ac 57 r sur #66' in current_address
    assert 'Ac 57 r sur #66' in permanent_address

@when('the user fills in the form with some fields missing')
def step_impl(context):
    context.text_box_page.fill_form(
        'Camila Alejandra Suarez Urrego',
        '',
        'Ac 57 r sur #66',
        'Ac 57 r sur #66'
    )
    context.text_box_page.submit_form()

@then('the user should see the filled fields in the output container')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'border'))
    )

    name, email, current_address, permanent_address = context.text_box_page.get_output()

    assert 'Camila Alejandra Suarez Urrego' in name
    assert '' == email
    assert 'Ac 57 r sur #66' in current_address
    assert 'Ac 57 r sur #66' in permanent_address

@when('the user fills in the form with empty fields')
def step_impl(context):
    context.text_box_page.fill_form('', '', '', '')
    context.text_box_page.submit_form()

@then('the user should not see the output container if all fields are empty')
def step_impl(context):
    output = context.driver.find_elements(By.CLASS_NAME, 'border')
    assert len(output) == 0

@when('the user fills in the form with only one field filled')
def step_impl(context):
    context.text_box_page.fill_form(
        'Camila Alejandra Suarez Urrego',
        '',
        '',
        ''
    )
    context.text_box_page.submit_form()

@then('the user should see only the filled field in the output container')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'border'))
    )

    name, _, _, _ = context.text_box_page.get_output()
    assert 'Camila Alejandra Suarez Urrego' in name
