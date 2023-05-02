from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.calculator.net/")
driver.implicitly_wait(10)

one = driver.find_element(By.XPATH , '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[1]')
two= driver.find_element(By.XPATH , '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[2]')
three = driver.find_element(By.XPATH , '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[3]')
four = driver.find_element(By.XPATH , '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[1]')
five = driver.find_element(By.XPATH , '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[2]')
six = driver.find_element(By.XPATH , '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[3]')
seven = driver.find_element(By.XPATH , '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[1]/span[1]')
eight = driver.find_element(By.XPATH , '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[1]/span[2]')
nine = driver.find_element(By.XPATH , '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[1]/span[3]')
zero = driver.find_element(By.XPATH , '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[4]/span[1]')

plus = driver.find_element(By.XPATH , '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[1]/span[4]')
minus = driver.find_element(By.XPATH , '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[4]')
multiplication = driver.find_element(By.XPATH , '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[4]')
division= driver.find_element(By.XPATH , '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[4]/span[4]')
equal = driver.find_element(By.XPATH , '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[4]')

ans = driver.find_element(By.XPATH , '//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[5]')
driver.implicitly_wait(5)

actions = ActionChains(driver)

# addition

actions.click(on_element=three)
actions.click(on_element=plus)
actions.click(on_element=nine)
actions.click(on_element=equal)
actions.perform()
time.sleep(1)
actions.click(on_element=ans)

time.sleep(2)

actions.click(on_element=seven)
actions.click(on_element=minus)
actions.click(on_element=two)
actions.click(on_element=equal)
actions.perform()
time.sleep(1)
actions.click(ans)

time.sleep(2)

actions.click(on_element=four)
actions.click(on_element=multiplication)
actions.click(on_element=five)
actions.click(on_element=equal)
actions.perform()
time.sleep(1)
actions.click(on_element=ans)

time.sleep(2)

actions.click(on_element=eight)
actions.click(on_element=division)
actions.click(on_element=two)
actions.click(on_element=equal)
actions.perform()
time.sleep(1)
actions.click(on_element=ans)

time.sleep(3)

print('Success')






