from pages.text_box import TextBox


def test_text_box(browser):
    name = 'Valery'
    address = 'Kushelevka'
    text_box_pg = TextBox(browser)
    text_box_pg.visit()

    text_box_pg.name.send_keys(text=name)
    text_box_pg.current_address.send_keys(text=address)
    text_box_pg.btn_submit.click()
    assert text_box_pg.sub_name.get_text() == "Name:" + name
    assert text_box_pg.sub_address.get_text() == "Current Address :" + address
