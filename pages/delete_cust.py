from selenium.webdriver.common.by import By


class DeleteCust:
    delete_customer = '//td[contains(text(),"Delete Customer")]'

    def __init__(self, driver):
        self.driver = driver

    def delete_cust(self):
        deleted = self.driver.find_element(By.XPATH, DeleteCust.delete_customer).click()
        try:
            deleted
        except:
            raise AssertionError
