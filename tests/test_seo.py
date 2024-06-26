from pages.demoqa import DemoQa
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab
import pytest
import time


def test_seo(browser):
    demoqa_pg = DemoQa(browser)
    demoqa_pg.visit()

    assert demoqa_pg.get_title() == 'DEMOQA'


@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'
