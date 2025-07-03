import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Click"))).click()


# Get list of all open window handles (main + child windows/tabs)
windowsOpened = driver.window_handles

# Store the handle of the main/original window
main_window = driver.current_window_handle

# Switch to the second window/tab (usually the new one)
#method1: note that your current window(mainwindow is in 0th index)
driver.switch_to.window(windowsOpened[1])
time.sleep(2)
#method2: when you have many
"""
for i in handles:
    if i!= main_window:
        driver.switch_to.window(i)
        break
"""

#print the text present in the child window:
childwindowText = driver.find_element(By.XPATH,"//h3")
print(childwindowText.text)

#close the child window
driver.close()

#return to main window
driver.switch_to.window(main_window)
print(driver.find_element(By.XPATH,"//h3").text)


time.sleep(2)
