"""
Scenario: Count the number of hyperlinks (<a> tags) on a page.
Website to Use: https://www.wikipedia.org/
Test Case: Count All Links Using TAG_NAME and print the first 5 link texts or hrefs to verify.
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.wikipedia.org/")
driver.maximize_window()

#TAG_NAME locator use panni elements ah find panalam.
#HTML tags example, <a>, <p>, <button>, <input>, <h1> ...(Inside < > is the HTML tag name.)
tag_names = driver.find_elements(By.TAG_NAME,"a")
time.sleep(2)

#len(tag_names) = total number of <a> tags in the page
print(f"Total number of links in this page are: {len(tag_names)}")
time.sleep(2)

#Loop-la first 5 <a> tags-oda href attribute (i.e., link URL)
total = 0
for tag in tag_names:
    name = tag.get_attribute("href")
    #get_attribute => attribute oda value edukum, like if <a href = 'sdf'> it will get sdf as result
    print(name)
    total = total + 1 #Counter increment pannrom after printing one link.
    if total>=5:
        break

time.sleep(2)
#output : https://en.wikipedia.org/ ,https://ja.wikipedia.org/, https://ru.wikipedia.org/ ,https://de.wikipedia.org/ ,https://es.wikipedia.org/

driver.quit()

