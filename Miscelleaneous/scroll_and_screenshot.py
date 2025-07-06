# Browsers are built on JavaScript,
# so some actions like scrolling, clicking hidden elements aren't possible using selenium.
# Selenium lets you run the Javascript from python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#to scroll by pixels, in Javascript we use: window.scrollTo(0,500);
#for executing this in selenium we use execute_script method
#syntax:driver.execute_script("javascript;")
scroll = WebDriverWait(driver,5)
scroll.until(EC.presence_of_element_located((By.TAG_NAME,"body")))

driver.execute_script("window.scrollTo(0,500);")
#this will scroll down 500 pixels vertically

#to scroll directly to the bottom of the page, we use
# javascript:  window.scrollTo(0,document.body.scrollHeight);
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

driver.implicitly_wait(5)
#you can take screen_shot and save it as file
driver.get_screenshot_as_file("sct.png")

