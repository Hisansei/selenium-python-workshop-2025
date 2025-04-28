from behave import given, when, then
from selenium import webdriver
from pages.intu_login_page import intuLogin

@given('el usuario se encuentra en la página login de intu')
def step_given_intu_login(context):
    context.driver = webdriver.Chrome() #Para mozilla webdriver.Firefox()
    context.driver.get('https://www.icesi.edu.co/moodle/login/index.php')
    context.intu_login_page = intuLogin(context.driver)

@when('el usuario ingresa credenciales erroneas')
def step_when_intu_login(context):
    context. intu_login_page.login('1144204560', 'Prueba')

@then('aparece un mensaje de error')
def step_then_intu_login(context):
    assert "Acceso inválido. Por favor, inténtelo otra vez." == context.intu_login_page.isElementPresent()