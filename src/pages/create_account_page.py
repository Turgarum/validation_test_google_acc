import time

class CreateAccount ():
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def FieldsFill (self,field_values):
        first_name_field = self.driver.find_element_by_id("firstName")
        last_name_field = self.driver.find_element_by_id("lastName")
        password_field = self.driver.find_element_by_name("Passwd")
        confirm_password_field = self.driver.find_element_by_name("ConfirmPasswd")

        first_name_field.send_keys(field_values['fn'])
        last_name_field.send_keys(field_values['ln'])
        password_field.send_keys(field_values['password'])
        confirm_password_field.send_keys(field_values['password'])

    def EmailFieldValidation (self,email_list,ValErrMsg):
        username_field = self.driver.find_element_by_id("username")
        next_button = self.driver.find_element_by_id("accountDetailsNext")
        for email in email_list:
            username_field.clear()
            username_field.send_keys(email)
            next_button.click()
            time.sleep(1)
            try:
                assert ValErrMsg in self.driver.page_source
                print ('Catched!')
            except AssertionError:
                print ('Not cathced!')


