# 미세먼지 농도 : 서울, 강남구
# api key : ------------------------------------------------------------------------

# api url : http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=stjlQoKqTsm4IBAGvPGwIa3rfwiC7FFtM9CkqUx7xxZInmSVJV09I8Fc9yPgArEEgkfnT%2BeSDxUg6uE6hp%2F7aA%3D%3D&numOfRows=10&pageNo=3&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0&returnType=json
import requests

serviceKey = '------------------------------------------------------------------------'                          # 주소 키 값
return_type = 'json'                                                                                             # 정보 표시 방법
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={serviceKey}&numOfRows=10&pageNo=3&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0&returnType={return_type}'
response = requests.get(url).json()                                                                              # url에서 받은 json 형식 정보
sido = response['response']['body']['items'][7]['sidoName']                                                      # 시도명 값
station = response['response']['body']['items'][7]['stationName']                                                # 지역명 값
pm10val = response['response']['body']['items'][7]['pm10Value']                                                  # 미세먼지 농도 값
pm25val = response['response']['body']['items'][7]['pm25Value']                                                  # 초미세먼지 농도 값
coval = response['response']['body']['items'][7]['coValue']                                                      # 일산화탄소 농도 값


print(f'{sido} {station}\n미세먼지 농도 = {pm10val}\n초미세먼지 농도 = {pm25val}\n일산화탄소 농도 = {coval}')

msg = f'{sido} {station}\n미세먼지 농도 = {pm10val}\n초미세먼지 농도 = {pm25val}\n일산화탄소 농도 = {coval}'      # 쳇봇이 전송할 메시지
token = '----------------------------------------------'                                                         # 쳇봇 접근용 토큰
url2 = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=1761910444&text={msg}'                          # 쳇봇 접근 url

response2 = requests.get(url2).json()                                                                            # 쳇봇에게 명령 전달(요청)