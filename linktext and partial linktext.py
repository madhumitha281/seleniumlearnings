"""
LINK_TEXT and PARTIAL_LINK_TEXT Locator Practice
Scenario: to click on a specific link by matching the visible text
Website to Use: https://demo.guru99.com/test/link.html
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#browser set panrom
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.guru99.com/test/link.html")
driver.maximize_window()

# sometimes oru popup varum, adhu handle panna try-except use panrom 
try:
    exi = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME,"cb-close")))
    exi.click()
except Exception as e:
    print("pop up not found",e)

#linktext
#<a href="http://www.google.com" style="font-size:16px;">click here</a>
click_here1 = driver.find_elements(By.LINK_TEXT,"click here")
click_here1[0].click()  #because andha page la two clickhere irruku, adhula first click here choose panrom
"""
#My mistake here
print(click_here.text)
prints the text of the old element (from the original page). 
Since the page has navigated to a new URL (http://www.google.com), 
this element no longer exists on the current page.
🔁 Instead, you should print the title or URL of the new page like this:
"""
#After navigation, explicit wait use panrom
#<input class="gNO89b" value="Google Search" aria-label="Google Search" name="btnK" role="button">
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.NAME, "btnK")))

print("1: ",driver.title) #for title
print(driver.current_url) #for the current url

# Go back to original page
driver.get("https://demo.guru99.com/test/link.html")

#partial link text
# "click here" second link
#<a href="http://www.fb.com" style="font-size:16px;">click here</a>
click_here2 = WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "click")))
click_here2[1].click()

#adutha page open aga wait panrom
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)
print("2: ",driver.title)
print(driver.current_url)