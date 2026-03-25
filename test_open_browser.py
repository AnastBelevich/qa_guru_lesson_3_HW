import time

from selene import browser, be, by, have

def test_successful_search():
    browser.open('https://duckduckgo.com/')
#if browser.element(by.text('Принять все')).matching(be.visible):
 #  browser.element(by.text('Принять все')).click()
    browser.element('#searchbox_input').should(be.blank).type('qa.guru').press_enter()
    browser.element('#r1-0 > div.ikg2IXiCD14iVX7AdZo1 > h2 > a > span').should(have.text("Курсы Тестировщиков"))
    time.sleep(5)


def test_unsuccessful_search():
    browser.open('https://duckduckgo.com/')
    browser.element('#searchbox_input').should(be.blank).type('1цывуа').press_enter()
    browser.element('#react-layout > div > div:nth-child(1) > div > div.FMPme3X940xAt4SKPFuw > section.At_VJ9MlrHsSjbfCtz2_.aDtqDaYogch0DyrGTrX6 > div > div > p > span').should(have.text("ничего не найдено."))
    time.sleep(5)


