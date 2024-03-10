using python selenium

 from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome browser
driver = webdriver.Chrome()

# Open Instagram page
driver.get("https://www.instagram.com/guviofficial/")

# Wait for the page to load
driver.implicitly_wait(10)

# Extract the total number of followers
followers_element = driver.find_element(By.XPATH, "//a[@href='/guviofficial/followers/']/span")
followers_count = followers_element.get_attribute("title")

# Extract the total number of following
following_element = driver.find_element(By.XPATH, "//a[@href='/guviofficial/following/']/span")
following_count = following_element.get_attribute("title")

print("Followers:", followers_count)
print("Following:", following_count)

# Close the browser
driver.quit() 

