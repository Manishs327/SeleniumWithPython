from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class Frame:

    def handle_frame_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.switch_to.frame(driver.find_element(By.ID,"iframeResult"))
        time.sleep(2)
        driver.switch_to.frame(0)
        time.sleep(2)
        driver.find_element(By.PARTIAL_LINK_TEXT,"Sign Up").click()
        time.sleep(10)

frame=Frame()
frame.handle_frame_demo()
