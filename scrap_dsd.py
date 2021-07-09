# This file from Data Science Dojo tutorial
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

URL = 'https://www.newegg.com/p/pl?N=100023083%20600481395&cm_sp=Cat_Home-Audio_6-_-VisNav-_-Bluetooth-Speakers_1&page=1'
page = requests.get(URL)
result = soup(page.content, "html.parser")

body_page = result.find(id="app")
product_containers = body_page.find_all('div', class_="item-cell")

# Product name


# print(result.h1)
# print(len(product_containers))
# #print(product_containers[0].prettify())
# #print(product_containers[0].div.div.div.a.prettify())
# #print(product_containers[0].div.div.div.a.img['title'])
# print(product_containers[0].find_all('a', class_='item-title')[0].text)
# print(product_containers[0].find('li', class_='price-ship').text)
# print(product_containers[1].find('span', class_='price-was-data').text)
# print(product_containers[0].find('span', class_='price-save-percent').text)
# print(product_containers[0].find('li', class_='price-current').text)
# price = product_containers[0].find('span', class_='price-was-data')
# price = '0' if price is None else price.text
# print(price)
# brand = product_containers[8].find('a', class_='item-brand') 
# brand = '' if (brand is None) or (brand.img is None) else brand.img['title']
# print(brand)
# rating = product_containers[0].find('a', class_='item-rating')['title']
# print(rating)
# rating_num = product_containers[0].find('span', class_='item-rating-num').text
# print(rating_num)
# brand = product.div.div.div.a

for product in product_containers:
    brand = product.find('a', class_='item-brand') 
    brand = 'na' if (brand is None) or (brand.img is None) else brand.img['title']

    product_name = product.find_all('a', class_='item-title')[0].text.strip()

    ship = product.find('li', class_='price-ship').text.strip()

    price = product.find('span', class_='price-was-data')
    price = '0' if price is None else price.text

    discount = product.find('span', class_='price-save-percent')
    discount = '0' if discount is None else discount.text

    current_price = product.find('li', class_='price-current').text

    rating = product.find('a', class_='item-rating')
    rating = 'na' if rating is None else rating['title']

    rating_num = product.find('span', class_='item-rating-num')
    rating_num = 'na' if rating_num is None else rating_num.text


    print('brand              : ', brand)
    print('product name       : ', product_name)
    print('shipping           : ', ship)
    print('price bfr discount : ', price)
    print('discount           : ', discount)
    print('Current price      : ', current_price)
    print('Rating             : ', rating)
    print('Rating number      : ', rating_num)
    print()
