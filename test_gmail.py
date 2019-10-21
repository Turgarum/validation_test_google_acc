from selenium import webdriver
import time
from src.pages.sign_in_page import SignInPage
from src.pages.create_account_page import CreateAccount

email_list = {'@a.a', 'a@-a.a', 'a@a@a.a', 'a@a'}
validation_error_message = 'Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.).'
user_dictionary = { 'fn':'Sergey', 'ln':'Cheshkov', 'password':'Abc123456!' }

driver = webdriver.Chrome('D:\QAA\chromedriver.exe')
driver.get('https://accounts.google.com')
driver.implicitly_wait(5)

sign_in_page = SignInPage(driver)
sign_in_page.create_account_action()

create_acc_validation = CreateAccount(driver)
create_acc_validation.FieldsFill(user_dictionary)

create_acc_validation.EmailFieldValidation(email_list,validation_error_message)

driver.close()