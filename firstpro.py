from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
'''
Always remember that your webdriver doesn't directly interact with chrome browser, 
it needs browser driver which is compatible for the chrome browser
we can use Webdriver_manager package which automatically downloads the 
latest browser driver for the browser we use! import it when using!
'''

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://support.google.com/")
driver.implicitly_wait(30)
driver.find_elements(By.ID,"youtube")
print("Page title: ", driver.title)

driver.quit()