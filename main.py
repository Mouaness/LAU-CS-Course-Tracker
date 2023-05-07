from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#get the username and password from the user
username = input("Enter your LAU username: ")
password = input("Enter your LAU password: ")

# Create a new Chrome webdriver instance
driver = webdriver.Chrome()

# Navigate to the LAU portal login page and wait for it to load
driver.get("https://banweb.lau.edu.lb/")
time.sleep(1)

# Enter the username and password in the input fields and submit the form
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys(username)
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(1)
driver.save_screenshot('screenshot.png')

#go to the student services and financial aid page
driver.find_element(By.XPATH, "//img[@alt='Student Services and Financial Aid']").click()
time.sleep(1)
driver.save_screenshot('screenshot1.png')

#go to the registration page
driver.find_element(By.XPATH, "//a[contains(@href, 'bmenu.P_RegMnu')]").click()
time.sleep(1)
driver.save_screenshot('screenshot2.png')

driver.close()