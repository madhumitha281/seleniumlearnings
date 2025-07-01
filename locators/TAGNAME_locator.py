"""
🔸 Scenario:
You want to count the number of hyperlinks (<a> tags) on a page.
🔹 Website to Use:
https://www.wikipedia.org/
🔹 Test Case: Count All Links Using TAG_NAME
Steps to Automate:
Open the Wikipedia homepage.
Use By.TAG_NAME to get all <a> elements.
Print the total number of links.
Optionally, print the first 5 link texts or hrefs to verify.
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


#installs the latest browser driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open the login page.
driver.get("https://www.wikipedia.org/")
driver.maximize_window()

#Use By.TAG_NAME to get all <a> elements.
tag_names = driver.find_elements(By.TAG_NAME,"a")
time.sleep(2)

#Print the total number of links.
print(f"Total number of links in this page are: {len(tag_names)}")
time.sleep(2)

#print the first 5 link texts or hrefs to verify.
i = 0
for tag in tag_names:
    name = tag.get_attribute("href")
    print(name)
    i = i + 1
    if i>=5:
        break

time.sleep(2)


