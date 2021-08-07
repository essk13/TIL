import requests
import random

token1 = '1880002910:AAE7zhKjWjVkV-nAM20TpHsQd--Stvaju28'
url = f'https://api.telegram.org/bot{token1}/getUpdates'
res = requests.get(url).json()

user_list = res['result']

chat_list = []
for user in user_list:
    # print(user['message']['chat']['id'])
    # print('-' * 20)
    chat_list.append(user['message']['chat']['id'])

chat_list = list(set(chat_list))

print(chat_list)

chat_id = random.choice(chat_list)

msg = f'{chat_id}'
token = '1815743270:AAFqabkm8r21q1OK-DtCm7JT0AbqHo0oKlY'
url1 = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=1761910444&text={msg}'

response = requests.get(url1).json()