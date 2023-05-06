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
time.sleep(10)