import requests, time, getpass, os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def cls():
    os.system('cls' if os.name=='nt' else 'clear')



options = webdriver.ChromeOptions()
options.add_argument("--log-level=OFF")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
url = "https://uclasurveys.co1.qualtrics.com/jfe/form/SV_3qRLtouCYKzBbH7"
driver.get(url)

print("\n\n---------------------------------------\n")

cls()

print("Selenium Started...")
time.sleep(0.1)
print("Symptom Monitoring Page Opened...\n")

USERNAME = "advit"
print("Stored UCLA Logon Username:", USERNAME)
PASSWORD = getpass.getpass('Please Enter Your Password: ')

print("\n")

# ------------------------------------------------------------------------- #

print("Moving Through Page 1...")

actions = ActionChains(driver)
actions.move_to_element_with_offset(driver.find_element(By.TAG_NAME, value='body'), 0,0)
actions.move_by_offset(200, -20).click().perform()

time.sleep(1)
actions.move_to_element_with_offset(driver.find_element(By.ID, value="NextButton"), 0,0).click().perform()
time.sleep(3)

# ------------------------------------------------------------------------- #

print("Moving through Page 2...")

inputID = driver.find_element(By.ID, value="logon")
inputID.send_keys(USERNAME)

time.sleep(1)

inputPass = driver.find_element(By.ID, value="pass")
inputPass.send_keys(PASSWORD)

time.sleep(1)
actions.move_to_element_with_offset(driver.find_element(By.NAME, value="_eventId_proceed"), 0, 0).click().perform()
time.sleep(1)


# ------------------------------------------------------------------------- #

print("Moving through Page 3...")

actions.move_to_element_with_offset(driver.find_element(By.TAG_NAME, value='body'), 0,0)
actions.move_by_offset(225, -20).click().perform()

current_url = driver.current_url
WebDriverWait(driver, 60).until(EC.url_changes(current_url))

# ------------------------------------------------------------------------- #

print("Moving through Page 4...")

time.sleep(1)
actions.move_to_element_with_offset(driver.find_element(By.ID, value="NextButton"), 0,0).click().perform()


# First, click the red button at the bottom of the screen (You have successfully signed in)

print("Moving through Page 5...")

time.sleep(1)
actions.move_to_element_with_offset(driver.find_element(By.ID, value="NextButton"), 0,0).click().perform()


# Next, click the red button at the bottom right of the screen (Your login information) 

print("Moving through Page 6...")

time.sleep(1)

actions.move_to_element_with_offset(driver.find_element(By.TAG_NAME, value='body'), 0,0)
actions.move_by_offset(200, -100).click().perform()

time.sleep(0.5)
actions.move_to_element_with_offset(driver.find_element(By.ID, value="NextButton"), 0,0).click().perform()


# Next, click "No" and then click the red button at the bottom right of the screen 

print("Moving through Page 7...")

time.sleep(1)

actions.move_to_element_with_offset(driver.find_element(By.TAG_NAME, value='body'), 0,0)
actions.move_by_offset(200, -100).click().perform()

time.sleep(0.5)
actions.move_to_element_with_offset(driver.find_element(By.ID, value="NextButton"), 0,0).click().perform()


print("\nCongrats, you've already completed your symptom monitoring!")

time.sleep(5)