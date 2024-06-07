from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/eelif/Desktop/SoftwareQuality/selenium/drivers/chromedriver.exe")

driver.maximize_window()
driver.get("https://www.google.com/maps/@40.9042944,29.2683776,12z?entry=ttu")
sleep(2)

# Gitmek istenilen konumu aratalım.
def searchplace():
    Place = driver.find_element(By.CLASS_NAME, "searchboxinput")
    Place.send_keys("Kocaeli Üniversitesi")
    Submit = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/div[1]/button/span")
    Submit.click()
searchplace()

# Yol tarfini seçsin.
def directions():
    sleep(10)
    directions = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button/span/span")
    directions.click()
directions()

# Başlangıç konumu arama yazsın.
def find():
    sleep(6)
    find = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
    find.clear()
    sleep(2)
    find.send_keys("Piri Reis Üniversitesi")
    sleep(6)
    search = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]/span")
    search.click()
find()

# En kısa güzergah kaç km söylesin.
def kilometers():
    sleep(3)
    Totalkilometers = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/div[1]/div[2]/div")
    print("Totalkilometers : ", Totalkilometers.text)
    driver.save_screenshot("ways.png")
kilometers()
driver.close()


