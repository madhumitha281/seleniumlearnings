import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
#Hover Over an Element
button = driver.find_element(By.ID,'mousehover')
driver.execute_script("arguments[0].scrollIntoView();", button)
actions = ActionChains(driver)
actions.move_to_element(button).perform()

#right click on the top
actions.context_click(driver.find_element(By.XPATH,"//a[text()='Top']")).perform()

time.sleep(3)




