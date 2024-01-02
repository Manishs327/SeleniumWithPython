from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
'''1. Open a driver'''
driver.get("https://www.google.com")
time.sleep(5)
driver.get("https://www.orangehrm.com/")

'''2. Click on an element'''
driver.find_element("xpath","//img[@alt='OrangeHRM Logo']").click()
print("I reached here")

'''3. Capture Title of the Page'''
title = driver.title

'''4. Capture Current URL'''
current_url=driver.current_url
print(title)
print(current_url)

'''5. Go to the backward page'''
driver.back()
time.sleep(5)
print(driver.title)
'''6. Navigate forward'''
driver.forward()
time.sleep(5)

'''7. Element is displayed'''
'''8. Element is enabled'''
driver.get("https://demo.guru99.com/test/newtours/")
ele = driver.find_element("name","userName");
print(ele.is_displayed())
print(ele.is_enabled())
print(ele.is_selected())

print(driver.title)

'''3. Close the driver'''
driver.close()

'''4. Quit the driver'''
driver.quit()
