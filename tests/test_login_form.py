from pages.form_page import FormPage
import time


def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()

    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys(text='tester')
    form_page.last_name.send_keys(text='testerovich')
    form_page.user_email.send_keys(text='test@ttt.tt')
    form_page.gender_radio_1.click()
    form_page.user_number.send_keys(text='9992223344')
    time.sleep(2)
    form_page.btn_submit.click()
    time.sleep(2)
