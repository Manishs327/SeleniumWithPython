import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class HandleMultipleWindows():
     def handle_window_demo(self):
         driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
         driver.maximize_window()
         driver.get("https://www.yatra.com")
         driver.implicitly_wait(20)
         parent=driver.current_window_handle
         ele = driver.find_element(By.XPATH,"//a[text()='View All']")
         driver.execute_script("arguments[0].click();",ele)
         driver.implicitly_wait(10)
         all_window=driver.window_handles

         for window in all_window:
             if(not window==parent):
                 driver.switch_to.window(window)
                 time.sleep(2)
                 print(driver.title)
                 time.sleep(2)
                 driver.close()
         driver.switch_to.window(parent)
         time.sleep(2)
         print(driver.title)
         time.sleep(5)

handle = HandleMultipleWindows()
handle.handle_window_demo()
