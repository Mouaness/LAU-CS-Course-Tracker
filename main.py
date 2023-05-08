from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import csv

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

#go to the look up classes page
driver.find_element(By.XPATH, "//a[text()='Look-up Classes to Add']").click()
time.sleep(1)
driver.save_screenshot('screenshot3.png')

#select the term from the drop down list
dropdown = driver.find_element(By.ID,'term_input_id')
select = Select(dropdown)
select.select_by_visible_text('Fall 2023 (View only)')
time.sleep(1)
driver.save_screenshot('screenshot4.png')

#submit the form
driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Submit']").click()
time.sleep(1)
driver.save_screenshot('screenshot5.png')

#go to the advanced search page
driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Advanced Search']").click()
time.sleep(1)
driver.save_screenshot('screenshot6.png')

#select the course from the drop down list
dropdown = driver.find_element(By.ID,'subj_id')
select = Select(dropdown)
select.select_by_visible_text('Computer Science')
time.sleep(1)
driver.save_screenshot('screenshot7.png')

#select the campus from the drop down list
dropdown = driver.find_element(By.ID,'camp_id')
select = Select(dropdown)

#deselect all options first
select.deselect_all()

#select the Byblos option using its value
select.select_by_value('2')
time.sleep(1)
driver.save_screenshot('screenshot8.png')

#section search
driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Section Search']").click()
time.sleep(1)
driver.save_screenshot('screenshot9.png')

driver.close()