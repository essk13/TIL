# age_api를 활용한 이름에 대한 평균 나이 정보 추출

import requests

url = 'https://api.agify.io?name=suhwan'  # 정보를 가져올 url
response = requests.get(url).json()       # json 형식으로 전달 받은 정보

print("{0} 이름의 사용자 평균 나이는 {1}입니다.".format(response['name'], response['age']))    # 정보 확인 및 추출


url2 = 'https://m.stock.naver.com/api/stocks/marketValue/KOSPI'  # 정보를 가져올 url
response2 = requests.get(url2).json()                            # json 형식으로 전달 받은 정보
 
print(response2)    # 정보 확인 및 추출