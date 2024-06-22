from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_navigation(browser):
    demo_qa_pg = DemoQa(browser)
    el_pg = ElementsPage(browser)

    demo_qa_pg.visit()
    demo_qa_pg.btn_elements.click()

    demo_qa_pg.refresh()
    browser.back()
    browser.forward()

    assert el_pg.equal_url()