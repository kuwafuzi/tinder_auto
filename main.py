import uc as uc
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException
import time
from pynput.keyboard import Key, Controller

facebook_email = "*********@******"
facebook_password = "***********"


# Get the URL
chrome_driver_path = "*****************************************"
#chrome_service = fs.Service(executable_path=chrome_driver_path)
#driver = webdriver.Chrome(service=chrome_service)
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = uc.Chrome(use_subprocess=True)
driver.maximize_window()
driver.get("https://tinder.com/")
parentGUID = driver.current_window_handle
time.sleep(70)

# Login to the tinder with facebook
mainmenu_login = driver.find_element(By.XPATH, '//*[@id="q-996647900"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
mainmenu_login.click()
time.sleep(70)
select_facebook_login = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
select_facebook_login.click()
time.sleep(70)

# get the All the session id of the browsers
handle_array = driver.window_handles
driver.switch_to.window(handle_array[1])

f_email_input = driver.find_element(By.ID, "email")
f_email_input.send_keys(facebook_email)
f_password_input = driver.find_element(By.ID, "pass")
f_password_input.send_keys(facebook_password)
f_login = driver.find_element(By.ID, "loginbutton")
f_login.click()
time.sleep(30)

# go back to the main window
driver.switch_to.window(parentGUID)

# click the agree button for location
location_agree = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div/div/div[3]/button[1]')
location_agree.click()
cookie_ok_button = driver.find_element(By.XPATH, '//*[@id="q-996647900"]/div/div[2]/div/div/div[1]/div[1]/button')
cookie_ok_button.click()
not_notification_button = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div/div/div[3]/button[2]')
not_notification_button.click()
time.sleep(10)


# I tried to click x botton, but it didn't work frequently and once it clicked, it didn't click again.
for i in range(30):
    time.sleep(4)
    try:
        print("called")
        not_interest_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[5]/div/div[2]/button')
        not_interest_button.click()
        time.sleep(4)
    except NoSuchElementException:
        print("except")
        not_interest_button_second = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[4]/div/div[2]/button')
        not_interest_button_second.click()
        time.sleep(4)
    except ElementClickInterceptedException:
        print("pop up message")
        pop_up_message = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div[2]/button[2]')
        pop_up_message.click()



# # This is a another solution using keyboard. I used left key instead of button, because x button is left key.
# for n in range(30):
#
#     # Add a 1 second delay between likes.
#     time.sleep(3)
#     try:
#         print("called")
#         body = driver.find_element(By.CSS_SELECTOR, 'body')
#         body.send_keys(Keys.LEFT)
#         time.sleep(4)
#
#     # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
#     except ElementClickInterceptedException:
#         try:
#             time.sleep(4)
#             not_add_home_screen = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div[2]/button[2]')
#             not_add_home_screen.click()
#         except NoSuchElementException:
#             continue
