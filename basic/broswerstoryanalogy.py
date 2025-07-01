import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


#installing browser driver 
chromeservice = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chromeservice)
#I need to open the browser to start the session!
# Removed duplicate driver line to avoid confusion
#to open the webpage, use get() method and give the link!
driver.get("https://www.bing.com/")

#Get the browser information like alerts, cookies, sites..etc
headline = driver.title 
print(headline) #this prints the title of the page
time.sleep(2)
#find the element (lcoaters and page elements like button, text..etc)
#this is the html code for the webpage we are using!
#for textbox, when you give inspect!
#<input class="sb_form_q" type="search" name="q" id="sb_form_q" maxlength="1000" />
fill_me = driver.find_element(By.ID, value = "sb_form_q")
time.sleep(2)
#for Bing search button
#<label for="search_icon" class="search icon tooltip"><input id="search_icon" class="search icon tooltip" type="submit" aria-label="Search" />
search_button = driver.find_element(By.ID, value = "search_icon")
time.sleep(2)

#Take actions on the elements
fill_me.send_keys("cat")
time.sleep(2)
search_button.click()
time.sleep(1.5)

#To check if the action you made got the response,
#Example title from search result
text_inside = driver.find_element(By.CLASS_NAME, "b_algo")
print(text_inside.text)

#you can use import time and time.sleep() for seeing the actions clearly!
time.sleep(5)
#to quit()
driver.quit()