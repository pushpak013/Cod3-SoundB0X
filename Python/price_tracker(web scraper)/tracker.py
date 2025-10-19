import requests
from datetime import datetime
from lxml import html



def get_price(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/118.0.5993.118 Safari/537.36',}
    responce = requests.get(url, headers)
    
    tree = html.fromstring(responce.text)
    
    title = tree.xpath('//*[@id="productTitle"]/text()')
    title = title[0].strip()
    
    price_whole = tree.xpath('//span[@class="a-price-whole"]/text()')
    price_fraction = tree.xpath('//span[@class="a-price-fraction"]/text()')

    if price_whole and price_fraction:
        price = f"{price_whole[0].strip()}.{price_fraction[0].strip()}"
    elif price_whole:
        price = price_whole[0].strip()
    else:
        price = "Price not found"

    #print(f'title: {title}\nprice: {price}')
    return title, price

#get_price()