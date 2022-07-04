from selenium.webdriver.common.by import By


class LoginPage:
    login_button = '//*[contains(text(),"Bank Manager Login")]'

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.find_element(By.XPATH, LoginPage.login_button).click()

