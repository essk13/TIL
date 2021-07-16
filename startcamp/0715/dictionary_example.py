# SW_Cp_2주차_04
# 딕셔너리 실습2


coin = {
    'BTC': {
        'opening_price': '44405000',
        'closing_price': '38806000',
        'min_price': '36640000',
        'max_price': '44999000',
        'prev_closing_price': '44404000',
        'fluctate_24H': '-7463000',
        'fluctate_rate_24H': '-16.13',
    },
    'ETH': {
        'opening_price': '1458000',
        'closing_price': '1229000',
        'min_price': '1100000',
        'max_price': '1490000',
        'prev_closing_price': '1458000',
        'fluctate_24H': '-275000',
        'fluctate_rate_24H': '-18.28',
    },
    'XRP': {
        'opening_price': '364.5',
        'closing_price': '311.9',
        'min_price': '284.2',
        'max_price': '372.7',
        'prev_closing_price': '364.2',
        'fluctate_24H': '-90.6',
        'fluctate_rate_24H': '-22.51',
    },
}

# 1. BTC의 max_price 값을 출력
# bitcoin = coin['BTC']
# print(bitcoin['max_price'])
# or
print((coin['BTC'])['max_price'])

# 2. BTC의 시가 + XRP의 시가 (시가 = opening_price)
# bitcoin = coin['BTC']
# bit_open = int(bitcoin['opening_price'])
# xrp = coin['XRP']
# xrp_open = float(xrp['opening_price'])
# print(bit_open + xrp_open)
# or
print(int((coin['BTC'])['opening_price']) + float((coin['XRP'])['opening_price']))