from bs4 import BeautifulSoup as soup
import requests

BASE_URL = 'https://www.newegg.com/p/pl?N=100023083%20600481395&cm_sp=Cat_Home-Audio_6-_-VisNav-_-Bluetooth-Speakers_1&page='
filename = 'portable_speaker.csv'
f = open(filename, 'w')

headers = "brand, product_name, shipping, price, discount, current_price, rating, rating_number\n"
f.write(headers)

for i in range(1, 21):
    URL = BASE_URL + str(i)
    page = requests.get(URL)
    result = soup(page.content, "html.parser")

    body_page = result.find(id="app")
    product_containers = body_page.find_all('div', class_="item-cell")

    for product in product_containers:
        brand = product.find('a', class_='item-brand') 
        brand = 'na' if (brand is None) or (brand.img is None) else brand.img['title']
        brand = brand.replace(',', '|')

        product_name = product.find_all('a', class_='item-title')[0].text.strip()
        product_name = product_name.replace(",", "|") # koma akan menggangu csv

        shipping = product.find('li', class_='price-ship').text.strip()

        price = product.find('span', class_='price-was-data')
        price = '0' if price is None else price.text

        discount = product.find('span', class_='price-save-percent')
        discount = '0' if discount is None else discount.text

        current_price = product.find('li', class_='price-current').text

        rating = product.find('a', class_='item-rating')
        rating = 'na' if rating is None else rating['title']

        rating_num = product.find('span', class_='item-rating-num')
        rating_num = 'na' if rating_num is None else rating_num.text

        f.write(brand + "," + product_name + ","+shipping+","+price+","+discount+","+current_price+","+rating+","+rating_num+"\n")
        print('brand              : ', brand)
        print('product name       : ', product_name)
        print('shipping           : ', shipping)
        print('price bfr discount : ', price)
        print('discount           : ', discount)
        print('Current price      : ', current_price)
        print('Rating             : ', rating)
        print('Rating number      : ', rating_num)
        print()

f.close()
