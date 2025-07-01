"""
Scenario:
Website to Use:
https://practicetestautomation.com/practice-test-login/

You are testing the login functionality of a demo web application.
Steps to Automate:
Open the login page. Locate the username field using its id.
Locate the password field using its id.
Enter the username: student
Enter the password: Password123
Locate and click the submit button using its id.
Verify successful login by checking:
The new page URL or A welcome message or Logout button appears
"""
import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#installs the latest browser driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.maximize_window()
#Locate the username field using its id.
#<input type="text" name="username" id="username" xpath="1">
#Enter the username: student
username = driver.find_element(By.ID,"username")
username.send_keys("student")
time.sleep(2)
#Locate the password field using its id.
#<input type="password" name="password" id="password" xpath="1">
#Enter the password: Password123
password = (driver.find_element(By.ID,"password"))
password.send_keys("Password123")
time.sleep(2)
#Locate and click the submit button using its id.
#<button id="submit" class="btn" xpath="1">Submit</button>
submit = driver.find_element(By.ID,"submit")
submit.click()
time.sleep(2)
#Verify successful login by checking:
#The new page URL or A welcome message or Logout button appears
check = driver.find_element(By.XPATH,"//h1[@class='post-title']").text
print("your welcome message: ", check)
assert check == "Logged In Successfully"
time.sleep(2)




