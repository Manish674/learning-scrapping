from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# setting browser to use  
driver = webdriver.Firefox()
driver.get("https://www.python.org")

# test case to see that the tab title says Python 
assert "Python" in driver.title

# html element
elem = driver.find_element(By.NAME, "q")
elem.clear()

# sending keyboard input 
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

# checking that some result was found and not No result 
assert "No results found" not in driver.page_source

driver.close()

