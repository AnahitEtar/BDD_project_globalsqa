from selenium.webdriver.common.by import By

from pages.submit_form import SubmitForm


class SearchCust:
    customers = '//button[@ng-class="btnClass3"]'
    search_customer = '//input[@type="text"]'

    def __init__(self, driver):
        self.driver = driver

    def search_cust(self):
        self.driver.find_element(By.XPATH, SearchCust.customers).click()
        a=self.driver.find_element(By.XPATH, SearchCust.search_customer).send_keys('Hakob')
        # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", Locators.cust_page)
