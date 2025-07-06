"""
You have a web table on a page — it has a column (like fruit/vegetable names).
When you click the column header, the table should sort alphabetically.

 Verify via automation that the table actually sorts correctly after the click.
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#click on the colum header of the table
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[text()='Top Deals']").click()
time.sleep(2)

handles = driver.window_handles
driver.switch_to.window(handles[1])  #switch to child window opened

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
time.sleep(2)
#collect all the items from the list
#//tr/td[1] this gets only veggies names in list
items = driver.find_elements(By.XPATH,"//tr/td[1]")
items_list = [i.text for i in items]

#before sorting, copy the original list
original_items = items_list.copy()

#sort the list
items_list.sort()

#Now compare the sorted list with the original list
assert items_list == original_items
print("Sorted!")

time.sleep(2)





