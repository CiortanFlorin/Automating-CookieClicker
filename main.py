from selenium import webdriver
import time

chrome_driver_path = "YOUR DRIVER PATH"
driver = webdriver.Chrome(executable_path = chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/?fbclid=IwAR2b7hU_K1Mr83aJL1-jQRUaDzlCn-VkT6X762UKKs8TDP4ZfI-d5GU1uy4/")

coockie = driver.find_element_by_id("cookie")

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

item_prices = []
all_prices = driver.find_elements_by_css_selector("#store b")
for n in all_prices:
    if n.text != '':
        item_prices.append(int(n.text.split(" ")[-1].strip().replace(',','')))

upgrades = {}
for n in range(len(item_prices)):
    upgrades[item_prices[n]]=item_ids[n]


print(upgrades)

timeout = time.time() + 5
five_min = time.time() + 5*60
while True:
    coockie.click()
    if time.time() > timeout:
        coockies_html = driver.find_element_by_id("money").text
        if "," in coockies_html:
            coockies_html = int(coockies_html.replace(',', ''))
        money = int(coockies_html)
        print(money)

        for n in item_prices:
            if money > n:
                expensive_id=upgrades[n]
        expensive_element = driver.find_element_by_id(expensive_id)
        expensive_element.click()
        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break