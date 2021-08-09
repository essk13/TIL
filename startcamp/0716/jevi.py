import requests
import random

token1 = 
url = 
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
token = 
url1 = 

response = requests.get(url1).json()