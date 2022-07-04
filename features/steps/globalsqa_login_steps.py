from behave import *
from selenium import webdriver
from pages.add_cust import AddCust
from pages.delete_cust import DeleteCust
from pages.login_page import LoginPage
from pages.search_cust import SearchCust
from pages.submit_form import SubmitForm


def __init__(self, driver):
    self.driver = driver


@given(u'I launch chrome browser')
def launch_browser(self):
    self.driver = webdriver.Chrome(executable_path='./chromedriver/chromedriver.exe')
    self.driver.implicitly_wait(10)


@when(u'I open globalsqa login page')
def open_globalsqa_login_page(self):
    self.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')


@then(u'I click Bank Manager Login button')
def verify_bank_manager_login_button(self):
    LoginPage.login(self)


@then(u'I click Add customer button')
def click_add_customer_button(self):
    AddCust.add_cust(self)


@then(u'I fill all fields and submit')
def fill_fields_and_submit_form(self):
    SubmitForm.f_name(self)
    SubmitForm.l_name(self)
    SubmitForm.p_code(self)
    SubmitForm.submit(self)
    SubmitForm.alert(self)


@then(u'I search added customer')
def search_customer(self):
    SearchCust.search_cust(self)


@then(u'I delete customer')
def delete_customer(self):
    DeleteCust.delete_cust(self)
    assert DeleteCust.delete_cust(self)


@then(u'I close browser')
def close_browser(self):
    self.driver.close()

