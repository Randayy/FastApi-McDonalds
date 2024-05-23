from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html"
driver.get(url)


products = driver.find_elements(By.CSS_SELECTOR, ".cmp-category__item[data-product-id] a")
products_links = [product.get_attribute("href") for product in products]
for link in products_links:
    driver.get(link)
    product_name = driver.find_element(By.CSS_SELECTOR, ".cmp-product-details-main__desktop-only span.cmp-product-details-main__heading-title").text
    product_small_desc = driver.find_element(By.CSS_SELECTOR, ".cmp-product-details-main__description div").text
    print({"name":product_name, "desc":product_small_desc})



driver.quit()
