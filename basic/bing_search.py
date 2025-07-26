#Task: enter text - give search

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


#first browser install panrom.
chromeservice = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chromeservice)

#get() method use panni website open panrom
driver.get("https://www.bing.com/")

#driver.title => page title print panrom, like bing, google..etc
print(driver.title)
time.sleep(2)

#textbox kitta inspect kudutha, html code irukum like this below,
#<input class="sb_form_q" type="search" name="q" id="sb_form_q" maxlength="1000" />

#locators (like ID,NAME...) use panni element find panitu, adhula text enter panrom.
fill_me = driver.find_element(By.ID, value = "sb_form_q")
fill_me.send_keys("cat")  #.send_keys => for entering text
time.sleep(2)

#search button locator find panrom, click action pannrom.
#<label for="search_icon" class="search icon tooltip"><input id="search_icon" class="search icon tooltip" type="submit" aria-label="Search" />
search_button = driver.find_element(By.ID, value = "search_icon")
search_button.click()
time.sleep(2)

#Search panna aprom result vandhucha nu check panna
text_inside = driver.find_element(By.CLASS_NAME, "b_algo")
print(text_inside.text)

#import time and time.sleep() => epdi automation nadakudhu nu konjam slow ah paaka idhu use aagum.
time.sleep(3)
#After use, browser ah full close panna quit() use panrom.
driver.quit()