from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class CheckBox:

    def checkbox_demo(self):
        driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.implicitly_wait(20)
        ele_check=driver.find_element(By.XPATH,"//input[@id='doi0']")
        time.sleep(20)
        print(ele_check.is_selected())
        if(not ele_check.is_selected()):
            ele_check.click()
            time.sleep(10)
        print(ele_check.is_selected())

check = CheckBox()
check.checkbox_demo()
