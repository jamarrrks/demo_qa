from pages.demoqa import DemoQa
import time


def test_size(browser):
    demoqa_pg = DemoQa(browser)
    demoqa_pg.visit()

    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)