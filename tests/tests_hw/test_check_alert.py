import time
from pages.alerts import Alerts


def test_check_alert(browser):
    alert_pg = Alerts(browser)
    alert_pg.visit()

    # проверяем, что на странице присутствует кнопка
    assert alert_pg.timer_btn.exist()
    alert_pg.timer_btn.click()
    # проверяем, что через 5 сек. после клика появляется alert
    time.sleep(6)
    assert alert_pg.alert()
