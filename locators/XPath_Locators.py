"""
✅ Practice Website:
🔗 https://www.saucedemo.com/
(Login: standard_user / secret_sauce)
//tag[@attr='value'] → Most common
//tag[contains(@attr,'val')] → When value may vary
//tag[text()='Exact Text'] → When matching full text
//tag[contains(text(),'partial')] → For partial match
//tag[1] → First matching tag
//tag[@class='a']/following-sibling::tag → Sibling navigation

"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.TAG_NAME,"body")))
#Absolute XPath -	/html/body/div/... (just for learning, not practical)
#Relative XPath -	//tagname[@attributename='value']
#<input class="input_error form_input" placeholder="Username" type="text" data-test="username" id="user-name" name="user-name" autocorrect="off" autocapitalize="none" value="">
username = driver.find_element(By.XPATH,"//input[@type='text']")
username.send_keys("standard_user")
#XPath with contains() -	//tagname[contains(@attribute, 'value')]
#Enter password secret_sauce using contains @name
#<input class="input_error form_input" placeholder="Password" type="password" data-test="password" id="password" name="password" autocorrect="off" autocapitalize="none" value="" xpath="1">
password = driver.find_element(By.XPATH,"//input[contains(@type,'password')]")
password.send_keys("secret_sauce")

#<input type="submit" class="submit-button btn_action" data-test="login-button" id="login-button" name="login-button" value="Login" style="" xpath="1">
#Click login using button text() - //tagname[text()='value'] ex: //h1[text()='Logged In Successfully']
#or //tagname[@id='value']
submit = driver.find_element(By.XPATH,"//input[@id='login-button']")
submit.click()

#Wait for product page and verify logo text Swag Labs
newpage = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.app_logo')))

assert newpage.text == "Swag Labs"
print(newpage.text)

#Click "Add to cart" on first item using following-sibling::
#Add to cart (first product)	(//button[text()='Add to cart'])[1]
first_item = driver.find_element(By.XPATH,"(//button[text()='Add to cart'])[1]")
print("Button text:", first_item.get_attribute("innerText"))
first_item.click()
#After clicking the add to cart, it will change into remove button.
#so to check the remove button appeared r not find the button again and assert

remove = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,"//button[@name = 'remove-sauce-labs-backpack']")))
assert remove.text == "Remove"
print("Button text:", remove.text)

driver.quit()


