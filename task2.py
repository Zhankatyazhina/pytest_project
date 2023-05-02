from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S839149522%3A1679889635919478&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&ifkv=AQMjQ7TNHBkV0Z0MySoOw-jbmdXg0lnJV4GmCs5COZUbVYFs01va0IqdVQdf_FIV4HcUq4zP9VfGgg&ltmpl=drive&passive=true&service=wise&usp=gtd&utm_campaign=web&utm_content=gotodrive&utm_medium=button&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.implicitly_wait(5)

email = driver.find_element(By.CSS_SELECTOR, 'input[type*=email]')
email.send_keys('200103326@stu.sdu.edu.kz')
email.send_keys(Keys.ENTER)
time.sleep(6)

password = driver.find_element(By.CSS_SELECTOR, 'input[type*=password]')
password.send_keys('Zhan.2003')
password.send_keys(Keys.ENTER)
time.sleep(5)

fromm = driver.find_element(By.XPATH, '//*[@data-tooltip="kids"]')
too = driver.find_element(By.XPATH, '//*[@data-tooltip="Parent"]')
my_drive = driver.find_element(By.XPATH , '//*[contains(@jsname="KSzLFd")]')

actions = ActionChains(driver)
actions.drag_and_drop(fromm, too).perform()
time.sleep(10)

actions.double_click(too).perform()
time.sleep(5)

action = ActionChains(driver)
action.drag_and_drop(fromm, my_drive).perform()
time.sleep(3)
