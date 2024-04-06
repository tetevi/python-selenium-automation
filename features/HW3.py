# 1. Find the most optimal locators for Create Account on amazon.com (Registration) page elements:

# - Amazon logo: search by XPATH, "a-icon a-icon-logo"
#
# - Create account: search by XPATH, “a-spacing-small”
#
# - Your name field: search by ID, "ap_customer_name"
#
# - Mobile number or email field: search by ID, "ap_email"
#
# - Password field: search by ID, "ap_password"
#
# - Password at least 6 characters: search by XPATH, "a-alert-content"
#
# - Re-enter password: search by ID, "ap_password_check"
#
# - Continue button: search by ID, "continue"
#
# - Conditions of Use: search by XPATH, "Conditions of Use"
#
# - Privacy Notice: search by XPATH, "Privacy Notice"
#
# - Sign in: search by XPATH, "a-link-emphasis"


# 2. Create a test case using BDD that opens target.com, clicks on the cart icon and
# verifies that “Your cart is empty” message is shown:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# # 1. Open https://www.target.com/
# driver.get('https://www.target.com/')
#
# # 2. Click on Cart icon
# driver.find_element(By.CSS_SELECTOR, ".styles__CartIconDiv-sc-jff2tp-1.bECXM").click()
#
# sleep(6)
#
# # 3. Verify “Your cart is empty” message is shown
# actual_text = driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
#
# print(actual_text)
# print('Test Case Successful')

# 3. Create a test case using BDD to verify that a logged out user can navigate to Sign In:

# 1. Open https://www.target.com/
driver.get('https://www.target.com/')

# 2. Click Sign In
driver.find_element(By.XPATH, "//span[text()='Sign in']").click()

# 3. From right side navigation menu, click Sign In
driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()

sleep(6)

# 4. Verify Sign In form opened
actual_text = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
print(actual_text)
print('Test Case Successful')
