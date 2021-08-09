# Naver_Developers_api

import requests
from pprint import pprint

query = '닌텐도스위치'        # input('제품명: ')
sort = 'asc'                  #input('정렬 옵션 (date, asc<오름차순>, dsc<내림차순>): ')
url =f'https://openapi.naver.com/v1/search/shop.json?query={query}&sort={sort}'

head = {
    'X-Naver-Client-Id': ,
    'X-Naver-Client-Secret': 
}

response = requests.get(url, headers = head).json()

# lprice = response['items'][0]['lprice']

lprice_title = ''
lprice_link = ''

for i in range(10):
    title = response['items'][i]['title']
    now_price =  int(response['items'][i]['lprice'])
    
    if i == 0:
        lprice_title = title
        lprice = now_price
        lprice_link = response['items'][i]['link']

    elif int(lprice) > now_price:
        lprice_title = title
        lprice = now_price
        lprice_link = response['items'][i]['link']

    print(f'제품명: {title}, 가격: {now_price}')

msg = f'최저가 제품명 : {lprice_title}\n가격: {lprice}\n구매링크: {lprice_link}'
token = '1815743270:AAFqabkm8r21q1OK-DtCm7JT0AbqHo0oKlY'
url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=1761910444&text={msg}'

response = requests.get(url).json()

pprint(response)