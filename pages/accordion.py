from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.section_content = WebElement(driver, '#section1Content > p')
        self.section_heading = WebElement(driver, '#section1Heading')

        self.def_section1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.def_section2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.def_section3 = WebElement(driver, '#section3Content > p')