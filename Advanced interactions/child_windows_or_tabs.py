import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/windows")

# Get list of all open window handles (main + child windows/tabs)
handles = driver.window_handles

# Store the handle of the main/original window
main_window = driver.current_window_handle

# Switch to the second window/tab (usually the new one)
driver.switch_to.window(handles[1])  # or whichever index you need
