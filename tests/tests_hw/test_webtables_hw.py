from pages.webtables import WebTables
import time


def test_case_1(browser):
    tables_pg = WebTables(browser)
    tables_pg.visit()

    first_name = 'Tester'
    last_name = 'Testerovich'
    email = 'test@ttt.tt'
    age = '10'
    salary = '10000'
    department = 'dept'

    tables_pg.btn_add.click()
    # проверяем, что появилась форма
    assert tables_pg.user_form.exist()
    tables_pg.btn_submit.click()
    # проверям, что была отправка пустой формы
    assert tables_pg.user_form.get_dom_attribute('class') == 'was-validated'

    tables_pg.first_name.send_keys(first_name)
    tables_pg.last_name.send_keys(last_name)
    tables_pg.user_email.send_keys(email)
    tables_pg.age.send_keys(age)
    tables_pg.salary.send_keys(salary)
    tables_pg.department.send_keys(department)
    tables_pg.btn_submit.click()
    time.sleep(2)
    # проверяем, что диалог закрылся
    assert not tables_pg.user_form.exist()
    # проверям, что в таблице появилась запись
    assert tables_pg.my_row.exist()
    # проверяем корректность данных
    assert tables_pg.my_row_first_name.get_text() == first_name
    assert tables_pg.my_row_last_name.get_text() == last_name
    assert tables_pg.my_row_age.get_text() == age
    assert tables_pg.my_row_email.get_text() == email
    assert tables_pg.my_row_salary.get_text() == salary
    assert tables_pg.my_row_department.get_text() == department

    tables_pg.btn_edit.click()
    # проверяем, что диалог открылся
    assert tables_pg.user_form.exist()
    # проверяем корректность данных
    assert tables_pg.first_name.get_dom_attribute('value') == first_name
    assert tables_pg.last_name.get_dom_attribute('value') == last_name
    assert tables_pg.user_email.get_dom_attribute('value') == email
    assert tables_pg.age.get_dom_attribute('value') == age
    assert tables_pg.salary.get_dom_attribute('value') == salary
    assert tables_pg.department.get_dom_attribute('value') == department

    # очистить
    tables_pg.first_name.clear()
    # вписать новое значение
    tables_pg.first_name.send_keys('Lera')
    tables_pg.btn_submit.click()
    assert tables_pg.my_row_first_name.get_text() == 'Lera'

    tables_pg.btn_delete.click()
    # проверяем, что из строки удалены данные
    assert tables_pg.my_row_first_name.get_text() == ' '
    assert tables_pg.my_row_last_name.get_text() == ' '
    assert tables_pg.my_row_age.get_text() == ' '
    assert tables_pg.my_row_email.get_text() == ' '
    assert tables_pg.my_row_salary.get_text() == ' '
    assert tables_pg.my_row_department.get_text() == ' '


def test_case_2(browser):
    tables_pg = WebTables(browser)
    tables_pg.visit()

    first_name = 'Tester'
    last_name = 'Testerovich'
    email = 'test@ttt.tt'
    age = '10'
    salary = '10000'
    department = 'dept'

    # установим кол-во строк 5
    tables_pg.btn_select.scroll_to_element()
    tables_pg.btn_select.click()
    tables_pg.btn_five.click()
    # проверим, что кнопки заблокированы
    assert tables_pg.btn_previous.get_dom_attribute('disabled')
    assert tables_pg.btn_next.get_dom_attribute('disabled')
    # добавим в таблицу 3 записи
    for i in range(3):
        tables_pg.btn_add.click()
        tables_pg.first_name.send_keys(first_name)
        tables_pg.last_name.send_keys(last_name)
        tables_pg.user_email.send_keys(email)
        tables_pg.age.send_keys(age)
        tables_pg.salary.send_keys(salary)
        tables_pg.department.send_keys(department)
        tables_pg.btn_submit.click()
    # проверим, что появилась вторая таблица
    assert tables_pg.total_pg_num.get_text() == '2'
    # кнопка Next доступна
    assert not tables_pg.btn_next.get_dom_attribute('disabled')
    tables_pg.btn_next.click()
    # при клике переход на страницу 2
    assert tables_pg.page_num.get_dom_attribute('value') == tables_pg.total_pg_num.get_text() == '2'
    # кнопка Previous доступна
    assert not tables_pg.btn_previous.get_dom_attribute('disabled')
    tables_pg.btn_previous.click()
    # при клике переход на страницу 1
    assert tables_pg.page_num.get_dom_attribute('value') == '1'



