#멋쟁이 사자처럼
#파이썬으로 만드는 게임
#AI 기능
def Updown():
    import random
    while(True):
       print("\n\nUpDown game starts!")
       print("===========================")
       limit = int(input("횟수 제한 숫자: "))
       print("\n범위를 설정하겠습니다.\n")
       first = int(input("시작 숫자 입력: "))
       second = int(input("끝 숫자 입력: "))
       print('\n{}부터 {}사이의 숫자로 게임을 시작하겠습니다!\n'.format(first, second))
       answer = random.randint(first, second)
       you_count = 0
       while you_count < limit:
            guess = int(input("\n{}~{} 사이 숫자를 찍어주세요: ".format(first,second)))
            print('you: ',guess)
            if guess <= second and guess >= first:
                if guess < answer:
                    print("UP!")
                elif guess > answer:
                    print("DOWN!")
                else:
                    print("you are Correct!!")
                    print("answer was",answer,"!!\n\n")
                    break
                computer_guess = random.randint(first, second)
                print('computer:', computer_guess)
                if computer_guess < answer:
                    print("UP!")
                elif computer_guess > answer:
                    print("DOWN!")
                else:
                    print("computer is Correct!!")
                    print("answer was", answer, "!!\n\n")
                print("남은 제한 횟수: ",limit - you_count-1,'번')    
                you_count = you_count + 1
            else:
                print("잘못 입력하셨습니다.")
                print("다시 입력해주세요.")
       if you_count == limit:
           print("\n\n제한 횟수를 초과했습니다.")
           print("게임을 다시 시작합니다.\n")
       

Updown()
