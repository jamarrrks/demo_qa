from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class WebElement:
    def __init__(self, driver, loc=''):
        self.driver = driver
        self.loc = loc

    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.loc)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)

    def visible(self):
        return self.find_element().is_displayed()
