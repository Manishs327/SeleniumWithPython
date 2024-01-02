from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Demo2:

    def find_by_tagname_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.implicitly_wait(20)
        num_frames=driver.find_elements(By.TAG_NAME,"iframe")
        print(len(num_frames))


    def find_list_of_element(self):
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com")
        driver.implicitly_wait(20)
        elements=driver.find_elements(By.XPATH,"//a")
        list_of_links=[]
        for ele in elements:
            list_of_links.append(ele.text)
        print(len(list_of_links))
        driver.quit()




demo=Demo2()
demo.find_list_of_element()
