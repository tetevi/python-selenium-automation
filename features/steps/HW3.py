from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# 2. Create a test case using BDD that opens target.com, clicks on the cart icon
# and verifies that “Your cart is empty” message is shown:
# @given('Open Target main page')
# def open_target(context):
#     context.driver.get('https://www.target.com/')
#
#
# @when('Click Cart icon')
# def click_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR, ".styles__CartIconDiv-sc-jff2tp-1.bECXM").click()
#     sleep(6)
#
#
# @then('Verify cart is empty')
# def verify_cart(context):
#     actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
#     print(actual_text)
#     print('Test Case Successful')


# 3. Create a test case using BDD to verify that a logged out user can navigate to Sign In:
@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()


@when('Click Sign In from nav menu')
def click_sign_in_nav(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()


@then('Verify Sign In form opened')
def verify_sign_in(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    print(actual_text)
    print('Test Case Successful')
