from pages.elements_page import ElementsPage


def test_elements(browser):
    el_pg = ElementsPage(browser)
    el_pg.visit()

    assert el_pg.btns_first_menu.check_count_elements(count=9)
