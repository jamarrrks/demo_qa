from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    mod_el_pg = ModalDialogs(browser)
    mod_el_pg.visit()

    assert mod_el_pg.btns.check_count_elements(count=5)


def test_navigation_modal(browser):
    mod_el_pg = ModalDialogs(browser)
    mod_el_pg.visit()
    browser.refresh()
    mod_el_pg.icon.click()

    # шаг назад стрелкой браузера
    browser.back()
    browser.set_window_size(900, 400)

    # шаг вперед стрелкой браузера
    browser.forward()
    assert browser.current_url == 'https://demoqa.com/'
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)



