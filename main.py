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

# Extract the data from the table and write it to a CSV file
with open('course_offerings.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header row
    header = ['Select', 'CRN', 'Course', 'Course number', 'section', 'campus', 'credits', 'Title', 'Days', 'Time', 'Cap', 'Act', 'Rem', 'WL Cap', 'WL Act', 'WL Rem', 'XL Cap', 'XL Act', 'XL Rem', 'Instructor', 'Date', 'Location', 'Attribute']
    writer.writerow(header)

    # Find all the rows in the table
    table = driver.find_element(By.XPATH, "//table[@class='datadisplaytable']")
    rows = table.find_elements(By.XPATH, "//tr")[1:]  # Skip the first row as it is the header

    # Loop through each row and extract the data
    count = 7
    for row in rows:
        if count == 0:
            cols = row.find_elements(By.XPATH, "./td")
            row_data = []
            for col in cols:
                row_data.append(col.text.strip()+"\t")
            if len(row_data) > 0:
                writer.writerow(row_data)
        else:
            count-=1


driver.close()