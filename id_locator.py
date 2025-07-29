"""
Scenario: Testing the login functionality of a demo web application.
Website to Use: https://practicetestautomation.com/practice-test-login/
username: student ; password: Password123
Verify successful login using A welcome message or The new page URL or Logout button appears 
"""
import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#browser open pannu
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#website link open pannu
driver.get("https://practicetestautomation.com/practice-test-login/")

driver.maximize_window()

#Task => ID locator use panni elements like username and password find panrom

#<input type="text" name="username" id="username" xpath="1">
username = driver.find_element(By.ID,"username")
username.send_keys("student")
time.sleep(2)

#<input type="password" name="password" id="password" xpath="1">
password = (driver.find_element(By.ID,"password"))
password.send_keys("Password123")
time.sleep(2)

#<button id="submit" class="btn" xpath="1">Submit</button>
submit = driver.find_element(By.ID,"submit")
submit.click()
time.sleep(2)

#Login aacha nu check panna assert keyword use panrom. checks if condition true else gives AssertionError

check = driver.find_element(By.XPATH,"//h1[@class='post-title']").text
print("your welcome message: ", check)
assert check == "Logged In Successfully"
time.sleep(2)

driver.quit()




