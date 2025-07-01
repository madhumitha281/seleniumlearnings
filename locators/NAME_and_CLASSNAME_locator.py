"""
🔹 Scenario:
You want to search for a product on an e-commerce demo site using the name attribute of the search input.
🔹 Website to Use:
https://www.saucedemo.com/
Steps to Automate:
Open the login page. Locate the username field using its name attribute.
Locate the password field using its name attribute.
Enter: Username: standard_user  ;  Password: secret_sauce
Locate and click the login button.
Verify login is successful by checking:
The new page URL is different, or Page title is visible, or You see a product container
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


#installs the latest browser driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open the login page.
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)
# Locate the username field using its name attribute.
#<input class="input_error form_input" placeholder="Username" type="text" data-test="username" id="user-name" name="user-name" autocorrect="off" autocapitalize="none" value="">
#Enter: Username: standard_user
username = driver.find_element(By.NAME,"user-name")
username.send_keys("standard_user")
time.sleep(2)

#Locate the password field using its name attribute.
#<input class="input_error form_input" placeholder="Password" type="password" data-test="password" id="password" name="password" autocorrect="off" autocapitalize="none" value="">
# Enter: Password: secret_sauce
password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")
time.sleep(2)

#Locate and click the login button.
#<input type="submit" class="submit-button btn_action" data-test="login-button" id="login-button" name="login-button" value="Login">
submit = driver.find_element(By.NAME,"login-button")
submit.click()
time.sleep(2)
#Verify login is successful by checking:
#<div class="app_logo">Swag Labs</div>
#using CLASS_NAME:
title = driver.find_element(By.CLASS_NAME,"app_logo").text
print("your app logo is ",title)
assert title == "Swag Labs"
time.sleep(2)