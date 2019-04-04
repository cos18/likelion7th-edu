import random as rand

# 숫자를 생성하는 함수 생성
    # - 겹치는 숫자가 없도록.
def make_random_number(length):
    result = ''
    finished = False
    while not finished:
        random_number = str(rand.randint(0,9))
        # 결과값에 이미 그 수가 있는지 검사
        if random_number in result:
            pass
        else:
            result = result + random_number
        # 결과값과 자릿수의 길이가 일치하는지 검사
        if length == len(result):
            finished = True
        else:
            pass
    return result


def check(correctanswer, count):
    
    answer=input("숫자를 입력해주세요. : ")
    print('현재 시도 횟수: ' + str(count))
    strike=0
    ball=0
    for i in range(length):
        for n in range(length):
            if correctanswer[i] == answer[n] and i == n:
                strike = strike + 1
            elif correctanswer[i] == answer[n] and i != n :
                ball = ball + 1
    if strike == length:
        print("{} 스트라이크! 승리했습니다.".format(length))
        # 정답을 맞추었을 때 횟수를 보여준다.
        print('{}회만에 맞추었습니다~!'.format(count))
        return strike
    elif strike == 0 and ball == 0:
        print("아웃!")
    else:
        print("{}스트라이크 {}볼".format(strike, ball))


# 사용자에게 원하는 자릿 수 입력받기
length = int(input('원하는 자릿수를 입력해주세요(다섯자리까지)'))
correctanswer = make_random_number(length)
print(correctanswer)

# 몇 번만에 맞추는지 보여주는 변수 선언
strike = 0
count = 0
A_TURN = True
############## 게임 ################
while strike != length:
    # A의 턴일 경우, A의 턴이라고 출력.
    if A_TURN:
        print('A의 턴입니다.')
    else:
        print('B의 턴입니다.')
    # 숫자를 입력받으면 count += 1
    count += 1
    strike = check(correctanswer, count)
    # 턴을 바꿔준다.
    A_TURN = not A_TURN
    print()

# 누구의 승리인지 표시한다.
A_TURN = not A_TURN
if A_TURN:
    print('A의 승리입니다.')
else:
    print('B의 승리입니다.')

# 벌칙을 랜덤하게 골라준다.
penalties = ['아이스크림 쏘기', '팔굽혀펴기 10개', '딱밤 3대', '100만원 주기', '학식 세 번 쏘기']
index = rand.randint(0, len(penalties)-1)
print('index는 ' + str(index))
print('벌칙은~~~~~' + penalties[index] + '입니다~~~~')
print()