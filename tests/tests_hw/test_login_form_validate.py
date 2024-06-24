import time

from pages.form_page import FormPage


def test_login_form_validate(browser):
    form_page = FormPage(browser)
    form_page.visit()

    assert form_page.first_name.get_dom_attribute(name='placeholder') == 'First Name'
    assert form_page.last_name.get_dom_attribute(name='placeholder') == 'Last Name'
    assert form_page.user_email.get_dom_attribute(name='placeholder') == 'name@example.com'
    assert form_page.user_email.get_dom_attribute(name='pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

    form_page.btn_submit.click_force()
    assert form_page.user_form.get_dom_attribute(name='class') == 'was-validated'


def test_state(browser):
    form_page = FormPage(browser)
    form_page.visit()

    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    form_page.btn_state.click()
    form_page.btn_NCR.click()
    time.sleep(2)


