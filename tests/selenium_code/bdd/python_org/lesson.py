from selenium import webdriver
from multiprocessing import Pool

def browser(url):
    browser = webdriver.Firefox()
    browser.get(url)
    browser.close()

p = Pool(10)
p.map(browser, [
    "https://www.google.co.jp",
    "http://www.yahoo.co.jp"
])