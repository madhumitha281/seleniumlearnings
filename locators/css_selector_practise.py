from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Use this site: https://practicetestautomation.com/practice-test-login/

"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.TAG_NAME,"body")))
"""
🔹 1. By ID
Selector: username
Action: Enter "student"
"""
#<input type="text" name="username" id="username">
by_ID = driver.find_element(By.CSS_SELECTOR,"#username")
by_ID.send_keys("student")

"""
🔹 2. By Class Name
Selector: .btn (submit button has this class)
✅ Task: Click the submit button
"""
#<button id="submit" class="btn">Submit</button>
by_class = driver.find_element(By.CSS_SELECTOR,".btn")
by_class.click()

"""
check if invalid message is coming
"""
#<div id="error" class="show">Your password is invalid!</div>
mes = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#error")))
assert mes.text == "Your password is invalid!"
print("success")

"""
🔹 3. By Tag Name
Selector: input, button, h1
✅ Task: Print all input field placeholders using:
"""
inputs = driver.find_elements(By.CSS_SELECTOR,"input")
for i in inputs:
    print("Placeholders: ",i.get_attribute("placeholder"))

"""
🔹 4. By Attribute
Selector: input[placeholder='Username'], input[type='password']
✅ Task: Fill password using attribute selector
"""
#<input type="text" name="username" id="username">  => username
#<input type="password" name="password" id="password">  => password
u_name = driver.find_element(By.CSS_SELECTOR,"input[type = 'text']")
u_name.send_keys("student")
p = driver.find_element(By.CSS_SELECTOR,"input[type = 'password']")
p.send_keys("Password123")

#<button id="submit" class="btn">Submit</button>  => submit butten
press = driver.find_element(By.CSS_SELECTOR,"button#submit")
#press = driver.find_element(By.CSS_SELECTOR,"button.btn")
press.click()

"""
🔹 5. Direct Child (>)
Selector: form > div > input
"""
#<div class="post-header">
#   <h1 class="post-title">Logged In Successfully</h1>
login = driver.find_element(By.CSS_SELECTOR,"div.post-header > h1")
assert login.text == "Logged In Successfully"
print(login.text)

"""
 6. nth-of-type / nth-child
Selector: form > div:nth-of-type(1) > input
✅ Task: Fill username using nth-type logic
"""
#<strong xpath="1">Congratulations student. You successfully logged in!</strong>
nth_child = driver.find_element(By.CSS_SELECTOR,"div.post-content > p:nth-child(1) > strong")
assert nth_child.text == "Congratulations student. You successfully logged in!"
print(nth_child.text)

"""
🔹 7. Extra: Combine Multiple Conditions using attribute
"""
#<a class="wp-block-button__link has-text-color has-background has-very-dark-gray-background-color" href="https://practicetestautomation.com/practice-test-login/" style="color:#ffffff" xpath="1">Log out</a>
logout = driver.find_element(By.CSS_SELECTOR, "a[style = 'color:#ffffff'][class = 'wp-block-button__link has-text-color has-background has-very-dark-gray-background-color']")
logout.click()
