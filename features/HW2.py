
# 1. Practice with locators. Create locators + search strategy

# - Amazon logo: search by XPATH, "a-icon a-icon-logo"
#
# - Email field: search by ID, “ap_email”
#
# - Continue button: search by ID, "continue"
#
# - Conditions of use link: search by XPATH, "Conditions of Use"
#
# - Privacy Notice link: search by XPATH, "Privacy Notice"
#
# - Need help link: search by XPATH, "a-expander-prompt"
#
# - Forgot your password link: search by ID, "auth-fpp-link-bottom"
#
# - Other issues with Sign-In link: search by ID, "ap-other-signin-issues-link"
#
# - Create your Amazon account button: search by ID, "createAccountSubmit"



# 2. Create a test case for the SignIn page using python & selenium script.

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

# 1. Open https://www.target.com/
driver.get('https://www.target.com/')

# 2. Click SignIn button
driver.find_element(By.XPATH, "//span[text()='Sign in']").click()

# 3. Click SignIn from side navigation
driver.find_element(By.XPATH, "//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl' and text()='Sign in']").click()

sleep(6)

# 4. Verify SignIn page opened
actual_text = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
print(actual_text)
print('Test Case Successful')



# [Optional]

# open the url
driver.get('https://www.target.com/')

# Enter 'coffee' in search field
driver.find_element(By.ID, 'search').send_keys('ps5')
# Click search btn
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

sleep(6)

# Verification
actual_text = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
assert 'ps5' in actual_text, f'Error! Text ps5 not in {actual_text}'
print(actual_text)
print('Test Case Successful')

driver.quit()








