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
validation_error_message = 'Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.).'

first_name_field = driver.find_element_by_id("firstName")
last_name_field = driver.find_element_by_id("lastName")
password_field = driver.find_element_by_name("Passwd")
confirm_password_field = driver.find_element_by_name("ConfirmPasswd")


username_field = driver.find_element_by_id("username")
next_button = driver.find_element_by_id("accountDetailsNext")
email_list = {'@a.a', 'a@-a.a', 'a@a@a.a', 'a@a'}
user_dictionary = { 'fn':'Sergey', 'ln':'Cheshkov', 'password':'Abc123456!' }

first_name_field.send_keys(user_dictionary['fn'])
last_name_field.send_keys(user_dictionary['ln'])
password_field.send_keys(user_dictionary['password'])
confirm_password_field.send_keys(user_dictionary['password'])

for email in email_list:
    username_field.clear()
    username_field.send_keys(email)
    next_button.click()
    time.sleep(1)
    assert validation_error_message in driver.page_source

driver.close()