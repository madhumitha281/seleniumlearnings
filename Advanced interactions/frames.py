from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://leafground.com/frame.xhtml")
driver.maximize_window()

"""
If you directly try to find this element, It throws a "NoSuchElementException" error
driver.find_element(By.XPATH,"//button[@id='Click']").click()
Hence first switch to the frame and then find the element
"""
iframe = driver.find_element(By.CSS_SELECTOR,"iframe[src='default.xhtml']")
driver.switch_to.frame(iframe)
driver.find_element(By.CSS_SELECTOR,'#Click').click()
textchange = driver.find_element(By.XPATH,"//button[text()='Hurray! You Clicked Me.']")
assert textchange.text == "Hurray! You Clicked Me."

driver.switch_to.default_content()






