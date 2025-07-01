"""
🔹 LINK_TEXT and PARTIAL_LINK_TEXT Locator Practice
🔸 Scenario:
You want to click on a specific link by matching the visible text.
🔹 Website to Use:
https://demo.guru99.com/test/link.html
🔹Test Case: Click a Link Using LINK_TEXT
Steps to Automate:
Open the demo link page.
Use By.LINK_TEXT to find and click the link that says "Click here".
Wait a bit and print the title or URL of the new page.
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#installs the latest browser driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open the login page.
driver.get("https://demo.guru99.com/test/link.html")
driver.maximize_window()

# ✅ Only use wait for popup — it’s dynamic
#you might get pop up like this
#<div data-v-17c36348="" class="cb-close" style="color: rgb(110, 117, 154);"></div>
try:
    exi = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME,"cb-close")))
    exi.click()
except Exception as e:
    print("pop up not found",e)

#linktext
# ✅ No need for wait here — page is static and loads instantly
#Use By.LINK_TEXT to find and click the link that says "click here".
#<a href="http://www.google.com" style="font-size:16px;">click here</a>
click_here1 = driver.find_elements(By.LINK_TEXT,"click here")
click_here1[0].click()
"""
#My mistake here
print(click_here.text)
prints the text of the old element (from the original page). 
Since the page has navigated to a new URL (http://www.google.com), 
this element no longer exists on the current page.
🔁 Instead, you should print the title or URL of the new page like this:
"""
# ✅ After navigation, use wait to ensure body is available
#<input class="gNO89b" value="Google Search" aria-label="Google Search" name="btnK" role="button">
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.NAME, "btnK")))

print("1: ",driver.title) #for title
print(driver.current_url) #for the current url

# Go back to original page
driver.get("https://demo.guru99.com/test/link.html")

#partial link text
# "click here" second link
#<a href="http://www.fb.com" style="font-size:16px;">click here</a>
# ✅ This page might take a sec — wait for links to appear

click_here2 = WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "click")))
click_here2[1].click()

# ✅ Wait again after navigation
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)
print("2: ",driver.title)
print(driver.current_url)