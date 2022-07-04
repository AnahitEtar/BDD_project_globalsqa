from selenium.webdriver.common.by import By


class AddCust:
    add_customer = '//button[@ng-class="btnClass1"]'

    def __init__(self, driver):
        self.driver = driver

    def add_cust(self):
        self.driver.find_element(By.XPATH, AddCust.add_customer).click()
