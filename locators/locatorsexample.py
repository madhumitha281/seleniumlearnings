import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("http://the-internet.herokuapp.com/login")

# 1. Locate username input (by ID)
# <input type="text" id="username">
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")
time.sleep(5)
# 2. Locate password input (by NAME)
# <input type="password" name="password">
password = driver.find_element(By.NAME, "password")
password.send_keys("SuperSecretPassword!")
time.sleep(5)
# 3. Locate submit button (by CSS selector)
# <button type="submit" class="radius">
submit_btn = driver.find_element(By.CSS_SELECTOR, "button.radius")
submit_btn.click()
time.sleep(5)
# 4. Get flash message (by XPATH)
# <div id="flash" class="flash success">
flash = driver.find_element(By.XPATH, "//div[@id='flash']")
print("Login message:", flash.text)

time.sleep(5)
driver.quit()
