from pages.text_box import TextBox


def test_placeholder(browser):
    text_box_pg = TextBox(browser)
    text_box_pg.visit()

    assert text_box_pg.name.get_dom_attribute(name='placeholder') == 'Full Name'

