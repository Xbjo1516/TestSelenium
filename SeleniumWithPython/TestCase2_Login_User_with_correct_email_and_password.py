from selenium import webdriver
from selenium.webdriver.common.by import By

import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()


try:
    driver.get("https://automationexercise.com/")
    assert "Automation Exercise" in driver.title
    print("Home page is visible successfully")

    driver.find_element(By.LINK_TEXT,"Signup / Login").click()
    Login = driver.find_element(By.XPATH, "//div[@class='login-form']/h2").text.strip()
    assert Login == "Login to your account"
    print("Load login page successfully")
    time.sleep(2)

    #0185
    driver.find_element(By.NAME,"email").send_keys("test0185@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("test0185")
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()
    time.sleep(2)

    username = driver.find_element(By.XPATH, "//li/a/b").text
    assert username == "test0185"
    print(f"Logged in as {username} is visible")

    driver.find_element(By.LINK_TEXT, "Delete Account").click()
    Delet = driver.find_element(By.XPATH, "//h2[@data-qa='account-deleted']").text.strip()
    assert Delet.upper() == "ACCOUNT DELETED!"
    print("ACCOUNT DELETED! is visible")

finally:
    driver.quit()