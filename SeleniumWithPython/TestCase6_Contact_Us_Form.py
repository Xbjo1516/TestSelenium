from selenium import webdriver
from selenium.webdriver.common.by import By

import time

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=option)
driver.maximize_window()

try:
    driver.get("https://automationexercise.com/")
    assert "Automation Exercise" in driver.title
    print("Home page is visible successfully")

    driver.find_element(By.LINK_TEXT,"Contact us").click()
    time.sleep(2)

    GetInTouch = driver.find_element(By.XPATH, "//h2[contains(text(),'Get In Touch')]").text.strip()
    assert GetInTouch.upper() == "GET IN TOUCH"
    print("GET IN TOUCH is visible")

    driver.find_element(By.NAME,"name").send_keys("test0185")
    driver.find_element(By.NAME,"email").send_keys("test0185@gmail.com")
    driver.find_element(By.NAME,"subject").send_keys("Test Subject")
    driver.find_element(By.NAME,"message").send_keys("This is a test message")

    path = r"C:\Users\supap\OneDrive - University of Phayao\Pictures\Camera Roll\download.jpg" #path ไฟล์ของตัวเองแ
    driver.find_element(By.NAME,"upload_file").send_keys(path)
    time.sleep(2)

    driver.find_element(By.NAME,"submit").click()

    #คลิกแจ้งเตือนของ Chrome
    alert = driver.switch_to.alert
    time.sleep(2)
    alert.accept() #อนุญาติ
    print("Alert accepted")

    submitted = driver.find_element(By.XPATH,'//div[@class="status alert alert-success"]').text
    assert submitted == "Success! Your details have been submitted successfully."
    print("success message")
    time.sleep(1)

    driver.find_element(By.LINK_TEXT,"Home").click()
    assert "Automation Exercise" in driver.title
    print("Home page is visible successfully")

finally:
    driver.quit()

# กด OK alert.accept()
# กด Cancel alert.dismiss()