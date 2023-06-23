from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")

# name of the saved contact that you want to send spam text to
target = '"Buddha"'
wait = WebDriverWait(driver, 10)

input("Press Enter when you have logged in whatsapp");
print("You are logged in!")

# find the contact
search_contact_xpath = '//span[contains(@title, ' + target + ')]'
target_elem = wait.until(
    EC.presence_of_element_located((By.XPATH, search_contact_xpath))
)

target_elem.click()

msg_box_xpath = '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'

msg_box_elem = wait.until(
    EC.element_to_be_clickable((By.XPATH, msg_box_xpath))
)

# text that you want to send
spam_text = ""

for i in range(100):
    for char in spam_text:
        msg_box_elem.send_keys(char)

    msg_box_elem.send_keys(Keys.ENTER)
    time.sleep(0.5)

input("Press enter to exit!")

driver.close()
