import requests
from datetime import datetime
from lxml import html



def get_price(url):
    print(f"Fetching URL: {url}")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/118.0.5993.118 Safari/537.36',}
#    responce = requests.get(url, headers)
    response = requests.get(url, headers=headers, timeout=10)
    print("Status:", response.status_code, "URL after redirects:", response.url)
    #print(response.text[:1000])

    
    tree = html.fromstring(response.text)
    
    title = tree.xpath('//*[@id="productTitle"]/text()')
    # title = title[0].strip()
    if title:
        title = title[0].strip()
    else:
        title = "Title not found"

    price_whole = tree.xpath('//span[@class="a-price-whole"]/text()')
    price_fraction = tree.xpath('//span[@class="a-price-fraction"]/text()')

    if price_whole and price_fraction:
        price = f"{price_whole[0].strip()}.{price_fraction[0].strip()}"
    elif price_whole:
        price = price_whole[0].strip()
    else:
        price = "Price not found"

    print(f'title: {title}\nprice: {price}')
    return title, price

get_price('https://www.amazon.in/Amazon-Multiport-Adapter-Aluminium-MacBook/dp/B0CFLT45KH/ref=pb_allspark_purchase_sims_desktop_d_sccl_2_3/520-5532928-7421420?pd_rd_w=sjERq&content-id=amzn1.sym.bf23bdc7-6f20-4210-b1c5-da3acd88edba&pf_rd_p=bf23bdc7-6f20-4210-b1c5-da3acd88edba&pf_rd_r=ETD48JH3JFFZ4N93FJT3&pd_rd_wg=F4Nfq&pd_rd_r=6620071d-e699-4b4b-878b-b27e4b9d02cb&pd_rd_i=B0CFLT45KH&psc=1')