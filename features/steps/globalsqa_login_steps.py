import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.locators import Locators


class GlobalsqaSteps(Locators):

    @given(u'launch chrome browser')
    def launch_browser(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver/chromedriver.exe')

    @when(u'open globalsqa login page')
    def open_globalsqa_login_page(self):
        self.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        time.sleep(3)

    @then(u'click Bank Manager Login button')
    def verify_bank_manager_login_button(self):
        self.driver.find_element(By.XPATH, Locators.login_button).click()
        time.sleep(2)

    @then(u'click Add customer button')
    def Add_customer(self):
        self.driver.find_element(By.XPATH, Locators.add_customer).click()
        time.sleep(2)

    @then(u'fill all fields and submit')
    def submit_form(self):
        self.driver.find_element(By.XPATH, Locators.first_name).send_keys('Hakob')
        self.driver.find_element(By.XPATH, Locators.last_name).send_keys('Hakobyan')
        self.driver.find_element(By.XPATH, Locators.post_code).send_keys('0034')
        self.driver.find_element(By.XPATH, Locators.add_customer_submit).click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()

    @then(u'search added customer')
    def search_customer(self):
        self.driver.find_element(By.XPATH, Locators.customers).click()
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", Locators.cust_page)
        assert 'Hakob Hakobyan 0034' in Locators.customers_list

    @then(u'delete customer')
    def delete_customer(self):
        self.driver.find_element(By.XPATH, Locators.delete_customer).click()

    @then(u'close browser')
    def close_browser(self):
        self.driver.close()

