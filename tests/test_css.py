from pages.text_box import TextBox


def test_text_box_submit(browser):
    text_box_pg = TextBox(browser)
    text_box_pg.visit()

    assert text_box_pg.btn_submit.check_css('color', 'rgba(255, 255, 255, 1)')
    assert text_box_pg.btn_submit.check_css('backgroundColor', 'rgba(0, 123, 255, 1)')
    assert text_box_pg.btn_submit.check_css('borderColor', 'rgb(0, 123, 255)')

