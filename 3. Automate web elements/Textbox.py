# Textbox – Send and Clear
#Textbox la either keys enter panrom or clear panrom. [.send_keys() ; .clear()]
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#browser setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#website
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

#textbox elements enga iruku nu locater use panni find pannitu adhula values add panrom

driver.find_element(By.CSS_SELECTOR,"#userName").send_keys("Honeymitha")
driver.find_element(By.CSS_SELECTOR,"input[type='email']").send_keys("honey888@udemy.com")
driver.find_element(By.CSS_SELECTOR,"#currentAddress").send_keys("23, tomoto road, potato colony")
driver.find_element(By.CSS_SELECTOR,"#permanentAddress").send_keys("90, temple road, neemtree junction")
time.sleep(2) #to see the actions
#submit button
submit = driver.find_element(By.CSS_SELECTOR,"button#submit")
scroll_to_click = submit.location_once_scrolled_into_view
#because scroll panama submit button click panna it will throw error, ElementClickInterceptedException: element click intercepted


