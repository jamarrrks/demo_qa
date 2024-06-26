from pages.alerts import Alerts
import time


# def test_alert(browser):
#     alert_pg = Alerts(browser)
#     alert_pg.visit()
#
#     assert not alert_pg.alert()
#     alert_pg.alert_btn.click()
#     time.sleep(2)
#     assert alert_pg.alert()


# def test_alert_text(browser):
#     alert_pg = Alerts(browser)
#     alert_pg.visit()
#
#     alert_pg.alert_btn.click()
#     time.sleep(2)
#     assert alert_pg.alert().text == 'You clicked a button'
#
#     alert_pg.alert().accept()
#     assert not alert_pg.alert()


# def test_confirm(browser):
#     alert_pg = Alerts(browser)
#     alert_pg.visit()
#
#     alert_pg.confirm_btn.click()
#     time.sleep(2)
#     alert_pg.alert().dismiss()
#     assert alert_pg.confirm_result.get_text() == 'You selected Cancel'


def test_prompt(browser):
    alert_pg = Alerts(browser)
    alert_pg.visit()

    alert_pg.prompt_btn.click()
    time.sleep(2)
    alert_pg.alert().send_keys('lera')
    alert_pg.alert().accept()
    assert alert_pg.prompt_result.get_text() == 'You entered lera'
