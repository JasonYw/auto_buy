import time
from playwright.sync_api import sync_playwright
from selenium import webdriver


def buy_selenium(pid):
    browser = webdriver.Chrome()
    browser.get("https://passport.jd.com/new/login.aspx")
    while True:
        if browser.current_url == "https://www.jd.com/":
            break
    browser.get(f"https://item.jd.com/{pid}.html")
    while True:
        selector = browser.find_element_by_link_text("加入购物车")
        if selector:
            selector.click()
            break
    browser.get("https://cart.jd.com/cart_index/")
    while True:
        selector = browser.find_element_by_link_text("去结算")
        if selector:
            selector.click()
            break
    while True:
        selector = browser.find_element_by_id("order-submit")
        if selector:
            selector.click()
            break
    time.sleep(1000)


# def buy(pid):
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto("https://passport.jd.com/new/login.aspx")
#         page.wait_for_url("https://www.jd.com/",timeout=500000)
#         try:
#             page.goto(f"https://item.jd.com/{pid}.html",timeout=1200)
#         except Exception as e:
#             pass
#         while True:
#             try:
#                 page.click(f'xpath=//a[@href="//cart.jd.com/gate.action?pid={pid}&pcount=1&ptype=1"]')
#                 break
#             except Exception as e:
#                 continue
#         page.goto("https://cart.jd.com/cart_index/")
#         page.click('text=去结算')
#         page.click('xpath=//div[@class="inner"]/button[@id="order-submit"]')
#         time.sleep(200)
# # https://plogin.m.jd.com/login/login?appid=300&returnurl=https%3A%2F%2Fwq.jd.com%2Fpassport%2FLoginRedirect%3Fstate%3D1101414989722%26returnurl%3Dhttps%253A%252F%252Fhome.m.jd.com%252FmyJd%252Fnewhome.action%253Fsceneval%253D2%2526ufc%253D%2526&source=wq_passport
# # https://item.jd.com/5028827.html
buy_selenium(5028827)
