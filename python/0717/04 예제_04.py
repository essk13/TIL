# 04 흐름과 제어 예제_04
# 다음의 결과와 같이 가상의 두 사람이 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오.
# 이 때 ["가위", "바위", "보"] 리스트를 활용합니다.

# input = 
# 바위
# 가위

# ouput = Result : Man1 Win!

Man1 = input('Man1 (가위, 바위, 보): ')
Man2 = input('Man2 (가위, 바위, 보): ')
rsp = ['가위', '바위', '보']

if Man1 == rsp[0]:
    if Man2 == rsp[1]:
        result = 'Man2 Win!'
    elif Man2 == rsp[2]:
        result = 'Man1 Win!'
        
elif Man1 == rsp[1]:
    if Man2 == rsp[0]:
        result = 'Man1 Win!'
    elif Man2 == rsp[2]:
        result = 'Man2 Win!'

elif Man1 == rsp[2]:
    if Man2 == rsp[0]:
        result = 'Man2 Win!'
    elif Man2 == rsp[1]:
        result = 'Man1 Win!'
    
if Man1 == Man2:
    result = 'Draw!' 
else:
    result = 'Error'

print(f'Result : {result}')