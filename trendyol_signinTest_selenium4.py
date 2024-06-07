#Selenium 4
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:/Users/eelif/Desktop/SoftwareQuality/selenium/drivers/msedgedriver.exe") #your path
driver = webdriver.Edge(service = serv_obj)

driver.maximize_window()
url = "https://www.trendyol.com/"
driver.get(url)
time.sleep(3)

driver.find_element(By.CLASS_NAME,"modal-close").click()
time.sleep(3)

Submit = driver.find_element(By.ID,"onetrust-accept-btn-handler")
Submit.click()

driver.find_element(By.CLASS_NAME,"link-text").click()
time.sleep(2)

driver.find_element(By.NAME,"login email").send_keys("your email enter") #enter yours
time.sleep(2)
driver.find_element(By.ID, "login-password-input").send_keys("your password enter") #enter yours
time.sleep(2)
driver.find_element(By.CLASS_NAME,"q-primary").click()
time.sleep(3)

driver.get(url+"/sepet")
time.sleep(2)
driver.back()
time.sleep(2)

act_title = driver.title
time.sleep(2)

exp_title = "En Trend Ürünler Türkiye'nin Online Alışveriş Sitesi Trendyol'da"
time.sleep(2)
if act_title == exp_title:
    print("Login Test Passed")
    print(driver.title)
else:
    print("Login Test Failed")
    print("Email or Password WRONG!")
driver.close()
