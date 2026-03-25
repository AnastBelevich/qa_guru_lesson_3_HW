import time, pytest
from selene import browser, be, by, have

@pytest.fixture
def open_browser():
    browser.open('https://duckduckgo.com/')
    browser.driver.set_window_size(1920, 1080)  # ✅ Ширина 1920px, высота 1080px
    # или browser.driver.maximize_window()  # Полноэкранный режим [[1]]

def test_successful_search(open_browser):
    browser.element('#searchbox_input').should(be.blank).type('qa.guru').press_enter()
    browser.element('#r1-0 > div.ikg2IXiCD14iVX7AdZo1 > h2 > a > span').should(have.text("Курсы Тестировщиков"))
    time.sleep(5)


def test_unsuccessful_search(open_browser):
    browser.element('#searchbox_input').should(be.blank).type('1цывуа').press_enter()
    browser.element('#react-layout > div > div:nth-child(1) > div > div.FMPme3X940xAt4SKPFuw > section.At_VJ9MlrHsSjbfCtz2_.aDtqDaYogch0DyrGTrX6 > div > div > p > span').should(have.text("ничего не найдено."))
    time.sleep(5)

def test_frov():
    browser.open('https://deor.frov-test.x5.ru')
    browser.element('#kc-form-login > div.h1').should(have.text("Вход"))
    time.sleep(5)



