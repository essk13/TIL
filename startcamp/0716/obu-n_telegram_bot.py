# telegram_chat_bot
# obu-n / Essk_13_bot

# <token> = 1815743270:AAFqabkm8r21q1OK-DtCm7JT0AbqHo0oKlY
# making_request_url = https://api.telegram.org/bot<token>/method
# chat_id = 1761910444

import requests

location = input("도시를 입력하세요(영문): ")
url1 = 'https://www.metaweather.com/api/location/search/?query=' + location
response1 = requests.get(url1).json()

woeid = response1[0]['woeid']
city = response1[0]['title']

date = input("날자를 입력하세요(년, 월, 일): ")
date = date.split(',')
date = list(map(int, date))
url2 = "https://www.metaweather.com/api/location/1132599/{0}/{1}/{2}/".format(date[0], date[1], date[2])
response2 = requests.get(url2).json()

weather = response2[0]['weather_state_name']
date2 = response2[0]["applicable_date"]

print(f"{city}의 {date2} 날씨는 {weather}로 예상됩니다.")

msg = f"{city}의 {date2} 날씨는 {weather}로 예상됩니다."
token = '1815743270:AAFqabkm8r21q1OK-DtCm7JT0AbqHo0oKlY'
url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=1761910444&text={msg}'

response = requests.get(url).json()

print(response)