import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("http://the-internet.herokuapp.com/login")

# 1.ID
# <input type="text" id="username">
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")
time.sleep(5)
# 2. NAME
# <input type="password" name="password">
password = driver.find_element(By.NAME, "password")
password.send_keys("SuperSecretPassword!")
time.sleep(5)
# 3. CSS_SELECTOR
# <button type="submit" class="radius">
submit_btn = driver.find_element(By.CSS_SELECTOR, "button.radius")  #tag_name.class method in css_selector
submit_btn.click()
time.sleep(5)
# 4. XPATH
# <div id="flash" class="flash success">
flash = driver.find_element(By.XPATH, "//div[@id='flash']")
print("Login message:", flash.text)

time.sleep(5)
driver.quit()
