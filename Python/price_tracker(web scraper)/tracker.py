import requests
from datetime import datetime
from lxml import html



def get_price(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.118 Safari/537.36',}
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

    print(f'title: {title}\nprice: {price}')

get_price('https://www.amazon.in/Apple-MacBook-13-inch-10-core-Unified/dp/B0DZDDQ429/ref=sr_1_3?crid=3UAA1KZLQHWCK&dib=eyJ2IjoiMSJ9.cxg64j71asHtIpoHuVSkM5Ehy5n1Z-roHbMIJOwdSihCb8PMv6P6B61WkDJUNes3Xs2wukMeiSQbEpltk7oxF5jj918ofZIUWZtQ2UT2F10RRWSN1zZSXFxpjgLJETWZT-3xYOFdTirNW9hnmIAOp4KjV36CwrenJ5Hicv7uclLZUqupeJ75TU_Gka7aIJNY_eCsDCYl6r99G6-Czv4xRgfxaDLjymwYzcnkAuX4xhI.mcIXVOB8qqe1ulMjo0sJMhLvvGpLbUeSZPSaUGoN7k4&dib_tag=se&keywords=mac%2Bbookair%2Bm4&qid=1760872014&sprefix=mac%2Bbook%2Caps%2C233&sr=8-3&th=1')