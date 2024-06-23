from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class WebElement:
    def __init__(self, driver, loc='', loc_type='css'):
        self.driver = driver
        self.loc = loc
        self.loc_type = loc_type

    def click(self):
        self.find_element().click()

    def click_force(self):
        self.driver.execute_script("arguments[0].click();", self.find_element())

    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.loc)

    def find_elements(self):
        return self.driver.find_elements(self.get_by_type(), self.loc)

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

    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements()) == count:
            return True
        else:
            return False

    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    def clear(self):
        self.send_keys(Keys.CONTROL + 'a')
        self.send_keys(Keys.DELETE)

    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        else:
            return True

    def get_by_type(self):
        if self.loc_type == "id":
            return By.ID
        elif self.loc_type == "name":
            return By.NAME
        elif self.loc_type == "xpath":
            return By.XPATH
        elif self.loc_type == "css":
            return By.CSS_SELECTOR
        elif self.loc_type == "class":
            return By.CLASS_NAME
        elif self.loc_type == "link":
            return By.LINK_TEXT
        else:
            print("Locator type" + self.loc_type + "not correct")
        return False

    def scroll_to_element(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);",
            self.find_element()
        )
