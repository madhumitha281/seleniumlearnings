"""
Scenario: Login Test Using Name and Class_name Locators
Website to Use: https://www.saucedemo.com/
Username: standard_user  ;  Password: secret_sauce
Verify login is successful
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)

# Task => Name locator use panni elements like username, password and login button find panrom

#<input class="input_error form_input" placeholder="Username" type="text" data-test="username" id="user-name" name="user-name" autocorrect="off" autocapitalize="none" value="">
username = driver.find_element(By.NAME,"user-name")
username.send_keys("standard_user")
time.sleep(2)

#<input class="input_error form_input" placeholder="Password" type="password" data-test="password" id="password" name="password" autocorrect="off" autocapitalize="none" value="">
password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")
time.sleep(2)

#<input type="submit" class="submit-button btn_action" data-test="login-button" id="login-button" name="login-button" value="Login">
submit = driver.find_element(By.NAME,"login-button")
submit.click()
time.sleep(2)

#Login successful aachi nu check panna first andha successful message element find panrom using CLASS_NAME
#<div class="app_logo">Swag Labs</div>

title = driver.find_element(By.CLASS_NAME,"app_logo").text
print("your app logo is ",title)
assert title == "Swag Labs"
time.sleep(2)

driver.quit()