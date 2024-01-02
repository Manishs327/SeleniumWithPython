import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class Act:

    def mouse_hover(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.yatra.com")
        driver.implicitly_wait(20)
        ele_to_move=driver.find_element(By.XPATH,"//span[contains(text(),'+ More')]")
        act = ActionChains(driver)
        act.move_to_element(ele_to_move).perform()
        time.sleep(3)
        ele_to_click=driver.find_element(By.XPATH,"//span[text()='Luxury Trains']")
        ele_to_click.click()
        time.sleep(10)

    def rightclick_demo(self):
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.implicitly_wait(20)
        ele_right_click = driver.find_element(By.XPATH,"//span[text()='right click me']")
        act=ActionChains(driver)
        act.context_click(ele_right_click).perform()
        time.sleep(4)
        driver.find_element(By.XPATH,"//span[text()='Cut']").click()
        print(driver.switch_to.alert.text)
        time.sleep(4)
        driver.switch_to.alert.accept()
        time.sleep(5)
        act.double_click(driver.find_element(By.XPATH,"//button[contains(text(),'Double-Click')]")).perform()
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.accept()
        time.sleep(5)

act = Act()
act.rightclick_demo()
