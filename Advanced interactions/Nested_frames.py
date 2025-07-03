from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://leafground.com/frame.xhtml")
driver.maximize_window()

iframe = driver.find_element(By.CSS_SELECTOR,"iframe[src='default.xhtml']")
driver.switch_to.frame(iframe)
driver.find_element(By.CSS_SELECTOR,'#Click').click()
textchange = driver.find_element(By.XPATH,"//button[text()='Hurray! You Clicked Me.']")
assert textchange.text == "Hurray! You Clicked Me."

driver.switch_to.default_content()
#now we got to the original DOM
#Lets move to next nested frames
iframe1 = driver.find_element(By.XPATH,"//iframe[@src='page.xhtml']")
iframe2 = driver.find_element(By.ID,"frame2")
driver.switch_to.frame(iframe1)
driver.switch_to.frame(iframe2)
clickHere = driver.find_element(By.ID,"Click")
clickHere.click()
assert clickHere.text == "Hurray! You Clicked Me."

driver.switch_to.default_content()
