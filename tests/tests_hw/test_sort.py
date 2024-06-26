from pages.webtables import WebTables


def test_sort(browser):
    tables_pg = WebTables(browser)
    tables_pg.visit()

    sort_result = 'rt-th rt-resizable-header -sort-asc -cursor-pointer'

    tables_pg.first_name_sort.click()
    assert tables_pg.first_name_sort.get_dom_attribute('class') == sort_result

    tables_pg.last_name_sort.click()
    assert tables_pg.last_name_sort.get_dom_attribute('class') == sort_result

    tables_pg.age_sort.click()
    assert tables_pg.age_sort.get_dom_attribute('class') == sort_result

    tables_pg.email_sort.click()
    assert tables_pg.email_sort.get_dom_attribute('class') == sort_result

    tables_pg.salary_sort.click()
    assert tables_pg.salary_sort.get_dom_attribute('class') == sort_result

    tables_pg.department_sort.click()
    assert tables_pg.department_sort.get_dom_attribute('class') == sort_result
