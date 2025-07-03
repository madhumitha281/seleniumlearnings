import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

#click the visible blinking link on the right top.
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME,"blinkingText"))).click()

newWindows = driver.window_handles
driver.switch_to.window(newWindows[1])  #switch to new child window

print("New child window opened: ", driver.title)

#copy mail id
mailID = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//strong/a"))).text
print(mailID)

driver.close()
driver.switch_to.window(newWindows[0])  #switch back to the original window

driver.find_element(By.NAME,"username").send_keys(mailID)
driver.find_element(By.ID,"password").send_keys("learning")
driver.find_element(By.ID,"terms").click()
driver.find_element(By.NAME,"signin").click()

error = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//div/strong"))).text

assert error == "Incorrect"
print(f"your password is {error}")












