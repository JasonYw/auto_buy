import time
from playwright.sync_api import sync_playwright
from selenium import webdriver
from logzero import logger
from multiprocessing import Process
import requests


def get_cookie(browser):
    browser.get("https://passport.jd.com/uc/login?ltype=logout")
    while True:
        if "www.jd.com" in browser.current_url:
            return browser.get_cookies()


def listen_item(browser, pid, cookies):
    browser.get("https://www.jd.com/")
    if isinstance(cookies, dict):
        browser.add_cookie(cookies)
    if isinstance(cookies, list):
        for i in cookies:
            browser.add_cookie(i)
    browser.get(f"https://item.jd.com/{pid}.html")
    while True:
        try:
            selector = browser.find_element_by_link_text("加入购物车")
            break
        except:
            browser.refresh()
    selector.click()
    logger.info(f"商品{pid}加入购物车")
    browser.close()
    return


def listen_cart(browser, pid, cookies):
    browser.get("https://www.jd.com/")
    if isinstance(cookies, dict):
        browser.add_cookie(cookies)
    if isinstance(cookies, list):
        for i in cookies:
            browser.add_cookie(i)
    browser.get("https://cart.jd.com/cart_index/")
    while True:
        try:
            selector = browser.find_element_by_link_text("去结算")
            break
        except:
            browser.refresh()
    selector.click()
    logger.info(f"商品{pid}开始结算")
    while True:
        try:
            selector = browser.find_element_by_id("order-submit")
            break
        except:
            browser.refresh()
    selector.click()
    logger.info(f"商品{pid}可以打开手机付款")
    browser.close()
    return


if __name__ == "__main__":
    browser_0 = webdriver.Chrome()
    cookies = get_cookie(browser_0)
    browser_0.close()
    opts = webdriver.ChromeOptions()
    # opts.set_headless()
    # browser_1 = webdriver.Chrome(chrome_options=opts)
    browser_2 = webdriver.Chrome(chrome_options=opts)
    # listen_item =Process(target=listen_item,args=(browser_1,100021367452,cookies))
    listen_cart = Process(target=listen_cart, args=(browser_2, 100021367452, cookies))
    # listen_item.start()
    listen_cart.start()
