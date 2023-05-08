# LAU-CS-Course-Tracker
This is a Python script that uses the Selenium library to scrape course offerings data from the Lebanese American University (LAU) portal. The script logs in to the portal, navigates to the Look-up Classes to Add page, selects a term and department, and extracts data from the resulting table. The data is then written to a CSV file named course_offerings.csv.

## Requirements
Python 3.x
Selenium library (pip install selenium)
Chrome browser (version 89 or higher)
Chrome webdriver for Selenium (version 89 or higher)

## Usage
1- Clone this repository to your local machine.
2- Install the required libraries as specified above.
3- Download the appropriate Chrome webdriver for your operating system and browser version and place it in the same directory as the script.
4- Open a terminal window in the directory containing the script and run the following command:
    python lau_scraper.py
5- Follow the prompts to enter your LAU username and password.
6- The script will launch a Chrome browser and navigate to the LAU portal. The scraping process may take a few minutes, depending on the number of courses offered in the selected department. The progress will be displayed in the terminal window.
7- Once the scraping is complete, the data will be saved to a CSV file named course_offerings.csv in the same directory as the script