from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import re
import requests
import json


driver = webdriver.Chrome()
url = "https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html"
driver.get(url)

products = driver.find_elements(By.CSS_SELECTOR, ".cmp-category__item[data-product-id]")
products_ids = [product.get_attribute("data-product-id") for product in products]
driver.quit()

items = []
for product_id in products_ids:
    url = f"https://www.mcdonalds.com/dnaapp/itemDetails?country=UA&language=uk&showLiveData=true&item={product_id}"
    headers = {
    'Referer': f'https://www.mcdonalds.com/ua/uk-ua/product/{product_id}.html',
    }
    response = requests.request("GET", url, headers=headers)

    data = response.json()
    try:
        item = {}
        item["name"] = data["item"]["item_name"]
        item["description"] = data["item"]["description"]
        item["weight"] = data["item"]["nutrient_facts"]["nutrient"][0]["value"]
        item["calories"] = data["item"]["nutrient_facts"]["nutrient"][2]["value"]
        item["proteins"] = data["item"]["nutrient_facts"]["nutrient"][7]["value"]
        item["fats"] = data["item"]["nutrient_facts"]["nutrient"][3]["value"]
        item["carbs"] = data["item"]["nutrient_facts"]["nutrient"][5]["value"]
        item["НЖК"] = data["item"]["nutrient_facts"]["nutrient"][4]["value"]
        item["Цукор"] = data["item"]["nutrient_facts"]["nutrient"][6]["value"]
        item["Ingridients"] = data["item"]["item_ingredient_statement"]
        item["Alergens"] = data["item"]["item_allergen"]
        items.append(item)
    except:
        pass
with open('items.json', 'w', encoding='utf8') as f:
    json.dump(items, f, ensure_ascii=False)

with open('items.json', 'r', encoding='utf8') as f:
    items = json.load(f)
    for x in items:
        print(x["proteins"])
