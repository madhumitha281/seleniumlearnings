from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
'''
WebDriver vandhu chrome browser-ah direct-ah control panna mudiyadhu.
Adhukaaga oru driver thevai, so "webdriver_manager" import pannnita, it will automatically downloads the latest browser driver.
'''


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://support.google.com/")

driver.implicitly_wait(5) #5 seconds wait pannum before going to next step!
driver.find_elements(By.ID,"youtube")
print("Page title: ", driver.title)

driver.quit()
