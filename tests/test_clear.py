from pages.text_box import TextBox
import time


def test_clear(browser):
    text_box_pg = TextBox(browser)
    text_box_pg.visit()

    text_box_pg.name.send_keys(text='tester')
    time.sleep(2)
    text_box_pg.name.clear()
    time.sleep(2)
    assert text_box_pg.name.get_text() == ''
