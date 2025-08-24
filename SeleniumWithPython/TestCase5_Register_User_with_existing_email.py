from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=option)
driver.maximize_window()

try:
    driver.get("https://automationexercise.com/")
    assert "Automation Exercise" in driver.title
    print("Home page is visible successfully")

    driver.find_element(By.LINK_TEXT,"Signup / Login").click()
    time.sleep(2)

    NewUser = driver.find_element(By.XPATH,'//div[@class="signup-form"]/h2').text
    assert NewUser == "New User Signup!"
    print("New User Signup is visible successfully")

    driver.find_element(By.NAME,"name").send_keys("test0185")
    driver.find_element(By.XPATH,'//input[@data-qa="signup-email"]').send_keys("test0185@gmail.com")
    driver.find_element(By.XPATH,'//button[@data-qa="signup-button"]').click()
    time.sleep(2)
    
    exist = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/p').text
    assert exist == "Email Address already exist!"  
    print("Email Address already exist! is visible")


finally:
    driver.quit()