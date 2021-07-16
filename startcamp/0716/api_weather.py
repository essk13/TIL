# api_weather를 이용한 지역 날씨정보 추출

import requests


# '서울 모레 날씨 {정보}로 예상됩니다.' 추출
# url = 'https://www.metaweather.com/api/location/1132599/2021/7/18/'
# response = requests.get(url).json()

# print(f"서울의 모레 날씨는 {response}로 예상됩니다.")


# upgrade_도시, 날짜 정보를 원하는 정보로 선택, 검색
location = input("도시를 입력하세요(영문): ")                                         # 검색할 도시명
url1 = 'https://www.metaweather.com/api/location/search/?query=' + location           # 검색한 도시에 대한 정보 url
response1 = requests.get(url1).json()                                                 # json 형식으로 전달 받은 정보
woeid = response1[0]['woeid']                                                         # 정보에서 추출한 woeid 값
city = response1[0]['title']                                                          # 정보에서 추출한 title(도시명) 값

date = input("날짜를 입력하세요(년, 월, 일): ")                                        # 검색할 날짜
date = date.split(',')
date = list(map(int, date))
url2 = "https://www.metaweather.com/api/location/1132599/{0}/{1}/{2}/".format(date[0], date[1], date[2])     # 검색에 대한 날씨 정보 url
response2 = requests.get(url2).json()                                                  # json 형식으로 전달 받은 정보
weather = response2[0]['weather_state_name']                                           # 정보에서 추출한 날씨 상태 값
date2 = response2[0]["applicable_date"]                                                # 정보에서 추출한 날짜 값

print("{0}의 {1} 날씨는 {2}로 예상됩니다.".format(city, date2, weather))