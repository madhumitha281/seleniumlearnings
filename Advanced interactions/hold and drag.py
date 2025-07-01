import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://jqueryui.com/droppable/")
driver.implicitly_wait(2)
# Switch to the iframe containing draggable/droppable elements using CSS selector
iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
driver.switch_to.frame(iframe)

source = driver.find_element(By.ID,"draggable")
dest = driver.find_element(By.ID,"droppable")
actions = ActionChains(driver)
actions.drag_and_drop(source,dest).perform()

time.sleep(3)