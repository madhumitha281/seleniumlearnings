import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

#task1: search for items named "ber"

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")

#task2: select the items that appear after search

items = WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div[class='product']")))
count = len(items)
#check the count of items should always be above zero
assert count > 0
print(count)
for i in items:
    #this is called chaining of parent to child web element
    if "ber" in i.find_element(By.CSS_SELECTOR, "h4.product-name").text.lower():
        i.find_element(By.CSS_SELECTOR, "div>button").click()

#task2.1: Assignment to list the items in the cart
Actual_list = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
cartItems = driver.find_elements(By.CSS_SELECTOR,"h4.product-name")
items_text = [i.text for i in cartItems]
print(items_text)

assert Actual_list == items_text
print("true")

#task3: click the cart and proceed to checkout
driver.find_element(By.CSS_SELECTOR,".cart-icon").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#task4: check the total amount of the items added matches the resulted amount

#for xpath => //tr/td[5]/p and for css => tr td:nth-child(5) p
prices = WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"tr td:nth-child(5) p")))
s = 0
for i in prices:
    s = s + int(i.text)

total = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert s == total
print(f"sum is {s} and total is {total}: Matched")

#task5: enter the promocode and click apply
code = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".promoCode")))
code.send_keys("rahulshettyacademy")

#click apply
apply = driver.find_element(By.CSS_SELECTOR,".promoBtn")
apply.click()

check = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
assert check.text == "Code applied ..!"
print(check.text)

#task6: Assignment:
# you apply discount and you get total after discount amount is less than the total amount
#check whether the total_amount is always greater than the total_after_discount

discount = int(driver.find_element(By.CSS_SELECTOR,".discountPerc").text.rstrip("%"))

print(total)
print(discount)
final_amt = total - (total * discount * 0.01)

tot_After_Discount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

print(f"final amount = {final_amt}")
assert final_amt == tot_After_Discount
print(f"total after discount = {tot_After_Discount}")

#but our main goal is whether total_amount is always greater than the total_after_discount
assert  total > tot_After_Discount
print("yes total_amount is always greater than the total_after_discount")



















time.sleep(3)