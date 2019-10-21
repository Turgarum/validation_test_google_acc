from selenium import webdriver
import time

driver = webdriver.Chrome('D:\QAA\chromedriver.exe')
driver.get('https://accounts.google.com')
driver.implicitly_wait(1)

create_account_button = driver.find_element_by_xpath("//*[text()='Создать аккаунт']")
create_account_button.click()

time.sleep(1)
#driver.implicitly_wait(1)

for_myself_button = driver.find_element_by_xpath("//*[text()='Для себя']")
for_myself_button.click()

first_name_field = driver.find_element_by_id("firstName")
last_name_field = driver.find_element_by_id("lastName")
password_field = driver.find_element_by_name("Passwd")
confirm_password_field = driver.find_element_by_name("ConfirmPasswd")


username_field = driver.find_element_by_id("username")
next_button = driver.find_element_by_id("accountDetailsNext")
email_list = {'@a.a', 'a@-a.a', 'a@a@a.a', 'a@a'}


first_name_field.send_keys("Sergey")
last_name_field.send_keys("Cheshkov")
password_field.send_keys("Abc123456!")
confirm_password_field.send_keys("Abc123456!")

for email in email_list:
    username_field.clear()
    username_field.send_keys(email)
    next_button.click()
    time.sleep(1)
    assert 'Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.).' in driver.page_source

driver.close()