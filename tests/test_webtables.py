from pages.webtables import WebTables
import time


def test_webtables(browser):
    tables_pg = WebTables(browser)
    tables_pg.visit()

    assert not tables_pg.no_data.exist()

    while tables_pg.btn_delete_row.exist():
        tables_pg.btn_delete_row.click()

    time.sleep(2)
    assert tables_pg.no_data.exist()
