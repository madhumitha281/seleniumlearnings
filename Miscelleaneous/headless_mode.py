"""
✅ What is headless mode?
Running a browser in headless mode means it operates without a visible GUI window
 — it executes normally but doesn’t display the browser on your screen.

✅ uses:
Run in environments without a display
Uses less CPU, memory, and GPU since there’s no need to draw the browser window.
Useful when running lots of parallel tests
    — avoids having dozens of browser windows popping up

✅ When not to use headless:
If you need to visually debug your automation scripts (e.g., watching where clicks happen).
If the site behaves differently in headless mode
— some sites detect headless browsers and block or render differently.

"""

#ChromeOptions is an object where you can set command-line arguments
# and preferences for how Chrome should start.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("headless")  #runs in headless mode
chrome_options.add_argument("window-size=1982,1080")  #sets the windows size

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
driver.quit()


