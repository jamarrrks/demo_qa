from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    accord_pg = Accordion(browser)
    accord_pg.visit()

    assert accord_pg.section_content.visible()
    accord_pg.section_heading.click()
    time.sleep(2)
    assert not accord_pg.section_content.visible()


def test_visible_accordion_default(browser):
    accord_pg = Accordion(browser)
    accord_pg.visit()

    assert not accord_pg.def_section1.visible()
    assert not accord_pg.def_section2.visible()
    assert not accord_pg.def_section3.visible()