from selenium import webdriver
import time

driver = webdriver.Chrome('D:\QAA\chromedriver.exe')
driver.get('https://accounts.google.com')
driver.implicitly_wait(1)

create_account_button = driver.find_element_by_xpath("//*[text()='Создать аккаунт']")
create_account_button.click()

time.sleep(1)

for_myself_button = driver.find_element_by_xpath("//*[text()='Для себя']")
for_myself_button.click()

first_name_field = driver.find_element_by_id("firstName")
first_name_field.send_keys("Sergey")

last_name_field = driver.find_element_by_id("lastName")
last_name_field.send_keys("Cheshkov")

password_field = driver.find_element_by_name("Passwd")
password_field.send_keys("Abc123456!")

confirm_password_field = driver.find_element_by_name("ConfirmPasswd")
confirm_password_field.send_keys("Abc123456!")

