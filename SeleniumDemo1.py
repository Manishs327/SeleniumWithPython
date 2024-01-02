from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoFindElement:

    def locate_by_id_or_name_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.implicitly_wait(20)
        #driver.find_element("id","login-input").send_keys("test@test.com")
        driver.find_element("id","login-input").send_keys("test@test.com")
        time.sleep(5)
        driver.quit()


    def locate_by_xpath_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.implicitly_wait(20)
        get_text=driver.find_element("xpath","//section[@class='pageheadings-block']/p[text()='Welcome to Yatra!']").text
        print(get_text)

    def locate_by_link_demo(self):
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        driver.implicitly_wait(20)
        driver.find_element(By.PARTIAL_LINK_TEXT,"Yatra for Business").click()
        driver.implicitly_wait(20)
        mytitle=driver.title
        print(mytitle)
findbyId= DemoFindElement()
findbyId.locate_by_link_demo()
