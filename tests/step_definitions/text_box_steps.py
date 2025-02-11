from behave import given, when, then
from config.config import create_driver, BASE_URL
from pages.text_box_page import TextBoxPage

@given('the user is on the Text Box page')
def step_impl(context):
    context.driver = create_driver()
    context.driver.get(BASE_URL)  # Usamos la URL desde la configuración
    context.text_box_page = TextBoxPage(context.driver)

@when('the user fills in the form with valid data')
def step_impl(context):
    context.text_box_page.enter_full_name('Camila Alejandra Suarez Urrego')
    context.text_box_page.enter_email('alejandra.urrego@outlook.com')
    context.text_box_page.enter_current_address('Ac 57 r sur #66')
    context.text_box_page.enter_permanent_address('Ac 57 r sur #66')
    context.text_box_page.click_submit()

@then('the user should see the correct submitted values')
def step_impl(context):
    assert "Name:Camila Alejandra Suarez Urrego" in context.text_box_page.get_name_output()
    assert "Email:alejandra.urrego@outlook.com" in context.text_box_page.get_email_output()
    assert "Current Address :Ac 57 r sur #66" in context.text_box_page.get_current_address_output()
    assert "Permanent Address :Ac 57 r sur #66" in context.text_box_page.get_permanent_address_output()

@then('the user should not see the output container if all fields are empty')
def step_impl(context):
    context.text_box_page.enter_full_name('')
    context.text_box_page.enter_email('')
    context.text_box_page.enter_current_address('')
    context.text_box_page.enter_permanent_address('')
    context.text_box_page.click_submit()
    assert "Name:" not in context.text_box_page.get_output_container_text()

@then('the user should see only the filled field in the output container')
def step_impl(context):
    context.text_box_page.enter_full_name('Camila Alejandra Suarez Urrego')
    context.text_box_page.enter_email('')
    context.text_box_page.enter_current_address('')
    context.text_box_page.enter_permanent_address('')
    context.text_box_page.click_submit()
    assert "Name:Camila Alejandra Suarez Urrego" in context.text_box_page.get_output_container_text()
    assert "Email:" not in context.text_box_page.get_output_container_text()

@then('the user should see error messages for missing fields')
def step_impl(context):
    context.text_box_page.enter_full_name('')
    context.text_box_page.enter_email('')
    context.text_box_page.enter_current_address('')
    context.text_box_page.enter_permanent_address('')
    context.text_box_page.click_submit()
    assert "Please fill out this field." in context.driver.page_source
