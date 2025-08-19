from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time

#การเปิดหน้าเว็บโดยไม่ปิดเอง
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

try:
    #Step 1 เปิดเว็บไซต์ และเช็กว่าเปิดแล้ว
    driver.get("https://automationexercise.com/")
    assert "Automation Exercise" in driver.title
    print("Home page loaded")
    time.sleep(2)

    #Step 2 
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    signup = driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/h2')
    assert signup.is_displayed()
    print("New User Signup!' is visible")
    time.sleep(2)
    
    #Step3
    driver.find_element(By.NAME,"name").send_keys("test0181")
    driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[3]').send_keys("test0181@gmail.com")
    btn = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/button').click()
    time.sleep(2)

    #Step4
    Account = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div[1]/h2')
    assert Account.is_displayed()
    print("Enter Account Information is visible")

    #Step5
    btn = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div[1]/form/div[1]/div[1]/label').click()
    driver.find_element(By.NAME,"password").send_keys("test0181")
    time.sleep(1)

    ##เลือกวันที่
    dropdown = Select(driver.find_element(By.ID,"days"))
    dropdown.select_by_visible_text("16")
    time.sleep(1)

    ##เลือกเดือน
    dropdown = Select(driver.find_element(By.ID,"months"))
    dropdown.select_by_visible_text("June")
    time.sleep(1)

    ##เลือกปี
    dropdown = Select(driver.find_element(By.ID,"years"))
    dropdown.select_by_visible_text("2000")
    time.sleep(1)

    #Step6
    driver.find_element(By.XPATH, '//*[@id="newsletter"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="optin"]').click()

    #Step7
    driver.find_element(By.NAME, "first_name").send_keys("test")
    driver.find_element(By.NAME, "last_name").send_keys("test")
    driver.find_element(By.NAME, "company").send_keys("automationexercise company")
    driver.find_element(By.NAME, "address1").send_keys("18/95")

    dropdown = Select(driver.find_element(By.ID, "country"))
    dropdown.select_by_visible_text("United States")
    driver.find_element(By.NAME, "state").send_keys("Arizona")
    driver.find_element(By.NAME, "city").send_keys("Phoenix")
    driver.find_element(By.NAME, "zipcode").send_keys("85029")
    driver.find_element(By.NAME, "mobile_number").send_keys("0558964821")
    time.sleep(2)

    #Step8
    btn = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div[1]/form/button').click()
    time.sleep(2)

    #Step9
    AccountCreated = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/h2/b')
    assert AccountCreated.is_displayed()
    print("Account Created is visible")

    #Step10
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()
    time.sleep(2)

    #Step11
    logged = driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]')
    assert logged.is_displayed()
    
    username = driver.find_element(By.XPATH, "//li/a/b").text
    
    assert username == "test0181"
    print(f"Logged in as {username} is visible")

    #Step12
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a').click()
    deleted_msg = driver.find_element(By.CSS_SELECTOR, "h2[data-qa='account-deleted']").text.strip()
    assert deleted_msg.upper() == "ACCOUNT DELETED!"
    print("ACCOUNT DELETED! is visible")

    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()

finally:
    driver.quit()