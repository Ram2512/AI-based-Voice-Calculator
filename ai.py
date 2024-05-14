# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


# Use Chrome as an example, make sure you have ChromeDriver installed
driver = webdriver.Chrome()

# Define the URL of the page you want to visit
url = "https://leetcode.com"

# Use Selenium to navigate to the desired webpage
driver.get(url)

# Wait for some time to ensure the page is fully loaded (you can adjust the time as needed)
# Wait for 10 seconds (you can change the wait time)
driver.implicitly_wait(10)

# Get the page source using Selenium
page_source = driver.page_source

# Parse the page source using BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Now you can work with the parsed HTML using BeautifulSoup
# For example, you can extract elements or perform further scraping operations

# Don't forget to close the WebDriver when you're done
driver.quit()
