from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class BrowserDemo:

    def browser_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        time.sleep(5)
        driver.maximize_window()
        time.sleep(5)
        driver.fullscreen_window()
        time.sleep(5)
        driver.get("https://www.yatra.com")
        time.sleep(5)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        time.sleep(5)
        driver.back()
        time.sleep(5)
        driver.forward()
        time.sleep(5)
        driver.minimize_window()
        time.sleep(5)
        driver.close()
        driver.quit()

browser_demo= BrowserDemo()
browser_demo.browser_demo()
