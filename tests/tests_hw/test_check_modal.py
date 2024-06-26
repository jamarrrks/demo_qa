import time
from pages.modal_dialogs import ModalDialogs


def test_check_modal(browser):
    modal_pg = ModalDialogs(browser)
    modal_pg.visit()
    # на странице присутствуют две кнопки
    assert modal_pg.small_modal_btn.exist()
    assert modal_pg.large_modal_btn.exist()

    # при клике на кнопку small modal появляется модальное окно
    modal_pg.small_modal_btn.click()
    time.sleep(2)
    assert modal_pg.modal_content.exist()
    # у окна есть кнопка close
    assert modal_pg.small_close_btn.exist()
    # по клику на кнопку close окно закрывается
    modal_pg.small_close_btn.click()
    time.sleep(2)
    assert not modal_pg.modal_content.exist()

    # при клике на кнопку large modal появляется модальное окно
    modal_pg.large_modal_btn.click()
    time.sleep(2)
    assert modal_pg.modal_content.exist()
    # у окна есть кнопка close
    assert modal_pg.large_close_btn.exist()
    # по клику на кнопку close окно закрывается
    modal_pg.large_close_btn.click()
    time.sleep(2)
    assert not modal_pg.modal_content.exist()
