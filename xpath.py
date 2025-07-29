"""
Practice Website: https://www.saucedemo.com/
(Login: standard_user / secret_sauce)
Types of Xpath we can use:
Absolute XPath -	/html/body/div/... (just for learning, not practical)
Relative Xpath: 
1) common ah use panra Xpath:        //tag[@attr='value']            
2) tag with partial attribute value: //tag[contains(@attr,'val')]    
3) When matching full text:          //tag[text()='Exact Text']
4) Match partial visible text:       //tag[contains(text(),'partial')]
5) First matching tag:               //tag[1] 
6) Sibling navigation:               //tag[@class='a']/following-sibling::tag
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

#WebDriverWait() -> explicitly wait works with condition
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.TAG_NAME,"body")))

#Exact Text Match: //tag[text()='Exact Text']
page_name = driver.find_element(By.XPATH,"//div[text()='Swag Labs']")
print(f"Page title: {page_name.text}")

#//tagname[@attribute='value']
#<input class="input_error form_input" placeholder="Username" type="text" data-test="username" id="user-name" name="user-name" autocorrect="off" autocapitalize="none" value="">
username = driver.find_element(By.XPATH,"//input[@id='user-name']")
username.send_keys("standard_user")

#//tagname[contains(@attribute, 'value')]  -  tag with partial attribute value
#<input class="input_error form_input" placeholder="Password" type="password" data-test="password" id="password" name="password" autocorrect="off" autocapitalize="none" value="" xpath="1">
password = driver.find_element(By.XPATH,"//input[contains(@placeholder,'Pass')]")
password.send_keys("secret_sauce")

#login button click pannu
#<input type="submit" class="submit-button btn_action" data-test="login-button" id="login-button" name="login-button" value="Login" style="" xpath="1">
submit = driver.find_element(By.XPATH,"//input[@id='login-button']")
submit.click()

#Wait for product page 
newpage = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.app_logo')))

#verifying logo text Swag Labs
assert newpage.text == "Swag Labs"
print(newpage.text)

#Click "Add to cart" on first item using index
#Add to cart (first product)	(//button[text()='Add to cart'])[1]
first_item = driver.find_element(By.XPATH,"(//button[text()='Add to cart'])[1]")
print("Button text:", first_item.get_attribute("innerText"))
first_item.click()

#Add to cart click panna, it will change into remove button, appo remove button vandhucha nu check pannanum

remove = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,"//button[@name = 'remove-sauce-labs-backpack']")))
assert remove.text == "Remove"
print("Button text:", remove.text)

driver.quit()


