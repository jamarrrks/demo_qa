from pages.links import Links
import time


def test_window_tab(browser):
    links_pg = Links(browser)
    links_pg.visit()

    assert links_pg.home_link.exist()
    assert links_pg.home_link.get_text() == 'Home'
    assert links_pg.home_link.get_dom_attribute('href') == 'https://demoqa.com'
    links_pg.home_link.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2
