# 06 함수의_기초_02
# 다음과 같이 사용자 2명으로부터 가위, 바위, 보를 입력 받아
# 위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성하십시오.

# input = 
# 홍길동
# 이순신
# 가위
# 바위
# output = 바위가 이겼습니다!

rsp = ['가위', '바위', '보']

def play_RSP():
    Player1 = input('Player1: ')
    Player2 = input('Player2: ')
    RSP_1 = input('Player1_RSP: ')
    RSP_2 = input('Player2_RSP: ')
    return RSP_1, RSP_2

def RSP_result(play_rsp):
    if play_rsp[0] == rsp[0]:
        if play_rsp[1] == rsp[1]:
            result = '바위가 이겼습니다!'
        elif play_rsp[1] == rsp[2]:
            result = '가위가 이겼습니다!'
        
    elif play_rsp[0] == rsp[1]:
        if play_rsp[1] == rsp[0]:
            result = '바위가 이겼습니다!'
        elif play_rsp[1] == rsp[2]:
            result = '보가 이겼습니다!'

    elif play_rsp[0] == rsp[2]:
        if play_rsp[1] == rsp[0]:
            result = '가위가 이겼습니다!'
        elif play_rsp[1] == rsp[1]:
            result = '보가 이겼습니다!'
    
    elif play_rsp[0] == play_rsp[1]:
        result = '비겼습니다!'
    
    elif play_rsp[0] != rsp or play_rsp[1] != rsp:
        result = 'Error'

    return result


RSP = play_RSP()
rsp_result = RSP_result(RSP)

print(rsp_result)