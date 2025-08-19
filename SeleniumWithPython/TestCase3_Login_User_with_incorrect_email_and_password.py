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
    

    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    Login = driver.find_element(By.XPATH, "//div[@class='login-form']/h2").text
    assert Login == "Login to your account"
    print("Login to your account is visible successfully")

    driver.find_element(By.NAME, "email").send_keys("testincorrect@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("testincorrect")
    time.sleep(1)
    driver.find_element(By.XPATH, '//button[@data-qa="login-button"]').click()

    Incorrect = driver.find_element(By.XPATH, "//form[@action='/login']/p").text
    assert Incorrect == "Your email or password is incorrect!"
    print("Your email or password is incorrect! is visible successfully")

finally:
    driver.quit()