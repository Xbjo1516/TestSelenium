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
    login = driver.find_element(By.XPATH,'//div[@class="login-form"]/h2').text
    assert login == "Login to your account"
    print("Login to your account is visible successfully")
    time.sleep(2)

    driver.find_element(By.NAME,"email").send_keys("test0185@gmail.com")
    driver.find_element(By.NAME,"password").send_keys("test0185")
    driver.find_element(By.XPATH,'//button[@data-qa="login-button"]').click()
    time.sleep(2)

    username = driver.find_element(By.XPATH,'//li/a/b').text
    assert username == "test0185"
    print(f"Logged in as {username} is visible")

    driver.find_element(By.LINK_TEXT,"Logout").click()
    time.sleep(2)
    
    assert login == "Login to your account"
    print("Login to your account is visible successfully")
finally:
    driver.quit()