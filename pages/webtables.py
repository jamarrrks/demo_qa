from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, 'div.action-buttons > span.Delete')

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.btn_submit = WebElement(driver, '#submit')
        self.user_form = WebElement(driver, '#userForm')

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')

        self.my_row = WebElement(driver, 'div.rt-table > div.rt-tbody > div:nth-child(4)')
        self.my_row_first_name = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(1)')
        self.my_row_last_name = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(2)')
        self.my_row_age = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(3)')
        self.my_row_email = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(4)')
        self.my_row_salary = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(5)')
        self.my_row_department = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(6)')

        self.btn_edit = WebElement(driver, '#edit-record-4')
        self.btn_delete = WebElement(driver, '#delete-record-4')

        self.btn_select = WebElement(driver, 'div.-center > span.select-wrap.-pageSizeOptions')
        self.btn_five = WebElement(driver, 'span.select-wrap.-pageSizeOptions > select > option:nth-child(1)')
        self.btn_previous = WebElement(driver, 'div.-previous > button')
        self.btn_next = WebElement(driver, 'div.-next > button')
        self.total_pg_num = WebElement(driver, 'div.-center > span.-pageInfo > span')
        self.page_num = WebElement(driver, 'div.-center > span.-pageInfo > div > input[type=number]')

        self.first_name_sort = WebElement(driver, 'div.rt-table > div.rt-thead.-header > div > div:nth-child(1)')
        self.last_name_sort = WebElement(driver, 'div.rt-table > div.rt-thead.-header > div > div:nth-child(2)')
        self.age_sort = WebElement(driver, 'div.rt-table > div.rt-thead.-header > div > div:nth-child(3)')
        self.email_sort = WebElement(driver, 'div.rt-table > div.rt-thead.-header > div > div:nth-child(4)')
        self.salary_sort = WebElement(driver, 'div.rt-table > div.rt-thead.-header > div > div:nth-child(5)')
        self.department_sort = WebElement(driver, 'div.rt-table > div.rt-thead.-header > div > div:nth-child(6)')

