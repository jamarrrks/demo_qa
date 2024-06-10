from pages.demoqa import DemoQa


def test_check_text1(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()

    # assert demo_qa_page.footer.exist()
    assert demo_qa_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_text2(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()

    demo_qa_page.btn_elements.click()
    # assert demo_qa_page.page_text.exist()
    assert demo_qa_page.page_text.get_text() == 'Please select an item from left to start practice.'

