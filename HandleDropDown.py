from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

class DropDown:

    def drop_down_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")
        driver.implicitly_wait(20)
        select = Select(driver.find_element(By.NAME,"UserTitle"))
        select.select_by_visible_text("Sales Manager")
        time.sleep(5)
        

    def multi_select(self):
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
        driver.implicitly_wait(20)
        ele=driver.find_element(By.NAME,"selenium_commands")
        select_DD=Select(ele)
        print(select_DD.is_multiple)
        select_DD.select_by_visible_text("Browser Commands")
        time.sleep(1)
        select_DD.select_by_index(4)
        time.sleep(2)
        select_DD.deselect_all()
        time.sleep(5)



dd = DropDown()
dd.multi_select()
