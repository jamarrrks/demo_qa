from pages.demoqa import DemoQa


def test_seo(browser):
    demoqa_pg = DemoQa(browser)
    demoqa_pg.visit()

    assert demoqa_pg.get_title() == 'DEMOQA'
