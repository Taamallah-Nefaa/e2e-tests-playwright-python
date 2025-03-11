from pages.login_page import LoginPage
from behave import given, when, then, step

@step('the user is on the account page')
def user_on_account_page(context):
    context.login_page = LoginPage(context.page)
    context.login_page.navigate()
    context.login_page.new_registration()

@when('User Enters A Username {username}')
def step_user_fill_in_username(context, username):
    #context.account_page = LoginPage(context.page)
    context.login_page.fill_username(username)

@when('User Enters A Password {password}')
def step_user_fill_in_password(context, password):
    #context.account_page = LoginPage(context.page)
    context.login_page.fill_password(password)


@when('User Clicks On Continue Button')
def step_click_on_continue(context):
    #context.account_page = LoginPage(context.page)
    context.login_page.click_on()
@then('User Should Be Logged In')
def step_user_should_be_logged_in(context):
    #context.account_page = LoginPage(context.page)
    context.login_page.assert_login()
