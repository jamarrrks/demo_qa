from pages.koup import Koup
from pages.koup_add import KoupAdd


def test_koup_add(browser):
    koup_pg = Koup(browser)
    koup_add_pg = KoupAdd(browser)
    koup_pg.visit()

    assert koup_pg.link_add.get_text() == 'Add/Remove Elements'
    koup_pg.link_add.click()
    assert koup_add_pg.equal_url()

    assert koup_add_pg.btn_add.get_text() == 'Add Element'
    assert koup_add_pg.btn_add.get_dom_attribute(name='onclick') == 'addElement()'

    for i in range(4):
        koup_add_pg.btn_add.click()

    assert koup_add_pg.btns_delete.check_count_elements(4)

    for elem in koup_add_pg.btns_delete.find_elements():
        assert elem.text == 'Delete'

    assert koup_add_pg.btns_delete.get_text() == 'Delete'

    while koup_add_pg.btns_delete.exist():
        koup_add_pg.btns_delete.click()

    assert not koup_add_pg.btns_delete.exist()

