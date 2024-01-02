from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
class ElemState:

    def is_enabled_demo(self):
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com")
        driver.implicitly_wait(20)
        bool1=driver.find_element(By.XPATH,"//a[@title='Round Trip']").is_enabled()
        bool2=driver.find_element(By.XPATH,"//a[@title='Round Trip']").is_displayed()
        bool3=driver.find_element(By.XPATH,"//a[@title='Non Stop Flights']/input").is_selected()
        print(bool1)
        print(bool2)
        print(bool3)
        driver.quit()

ele_state = ElemState()
ele_state.is_enabled_demo()
