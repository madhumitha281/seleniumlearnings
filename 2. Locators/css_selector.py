
"""
website: https://practicetestautomation.com/practice-test-login/
CSS_SELECTOR:

using ID: #id_value
using class: .class_value
using attribute: tag_name[attribute = 'value']
using tag & class: tag_name.class_value
using directchild: parent>child 
using order: tag_name:nth-child(n)  where n=position of the element

"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.TAG_NAME,"body")))

#using ID => use #id_value
#<input autocomplete="off" placeholder="Full Name" type="text" id="userName" class=" mr-sm-2 form-control">
name = driver.find_element(By.CSS_SELECTOR,"#userName")
name.send_keys("Honeymitha")

#using CLASS_NAME  =>  use .class_value
#<input autocomplete="off" placeholder="name@example.com" type="email" id="userEmail" class="mr-sm-2 form-control">
#here class la space iruku so it is not used directly, use one class name
#but inga class use pannala because in name also we have same class, appo username laye email print agum
#eppovum unique ah dhan choose pannanum for finding elements
email = driver.find_element(By.CSS_SELECTOR,"input[type='email']")
email.send_keys("honey345@yahoo.com")

#using attribute: tag_name[attribute = 'value']
#<textarea placeholder="Current Address" rows="5" cols="20" id="currentAddress" class="form-control"></textarea>
curr_adr = driver.find_element(By.CSS_SELECTOR,"textarea[id = 'currentAddress']")
curr_adr.send_keys("Gandhi road, near bharat petrol")

#using tag & ID: tag_name#id_value
#<textarea rows="5" cols="20" id="permanentAddress" class="form-control"></textarea>
per_adr = driver.find_element(By.CSS_SELECTOR,"textarea#permanentAddress")
per_adr.send_keys("same as current adress")

#<button id="submit" type="button" class="btn btn-primary">Submit</button>
submit = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button#submit")))

#indha following line use panala na error varudhu (ElementClickInterceptedException)
#scrollIntoView(true) → submit Button screen-la varanum, adha scroll panni bring pannum.
driver.execute_script("arguments[0].scrollIntoView(true);", submit)
#or use Action chains by importing it
#ActionChains(driver).move_to_element(submit).click().perform()
submit.click()

# using Order: tag_name:nth-child(n)
output_box = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#output>div:nth-child(2)")))
print("Output Line 2:", output_box.text)


