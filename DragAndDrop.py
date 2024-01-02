import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time


class DnD:

    def drag_and_drop_demo(self):
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://jqueryui.com/droppable/")
        driver.implicitly_wait(20)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME,"iframe"))
        time.sleep(5)
        ele_drag=driver.find_element(By.XPATH,"//div[@id='draggable']")
        ele_drop=driver.find_element(By.XPATH,"//div[@id='droppable']")
        act=ActionChains(driver)
        act.drag_and_drop(ele_drag,ele_drop).perform()
        time.sleep(10)

dnd = DnD()
dnd.drag_and_drop_demo()
