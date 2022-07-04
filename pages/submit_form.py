from selenium.webdriver.common.by import By


class SubmitForm:
    first_name = '//input[@ng-model="fName"]'
    last_name = '//input[@placeholder="Last Name"]'
    post_code = '//input[@placeholder="Post Code"]'
    add_customer_submit = '//button[@type="submit"]'

    def __init__(self, driver):
        self.driver = driver

    def f_name(self):
        self.driver.find_element(By.XPATH, SubmitForm.first_name).send_keys('Hakob')

    def l_name(self):
        self.driver.find_element(By.XPATH, SubmitForm.last_name).send_keys('Hakobyan')

    def p_code(self):
        self.driver.find_element(By.XPATH, SubmitForm.post_code).send_keys('0034')

    def submit(self):
        self.driver.find_element(By.XPATH, SubmitForm.add_customer_submit).click()

    def alert(self):
        self.driver.switch_to.alert.accept()