import random
import sys

#1횟수제한 
#2범위설정 format, map, split   ;;
#3다시하기 function  
#4
#4범위 벗어나는 숫자 입력 하면 알려주기 ;;
#5남은횟수알려주기 format
#6다시하고 종료 하면 종료
#7게임 실행 횟수 알려주기 
#8빨리 맞출수록 점수 높다

# 문제 3,4번 리뷰 하면서 행맨 게임의 경우 단어지정하기, 단어꺼내쓰기, 단어 랜덤으로 설정하기 리뷰
# append , list ,map, split, format 간략한 설명
# 횟수제한, 범위설정, 함수로 코드 다시쓰기, 범위 벗어난 숫자 다시 알려주기 
# 운영진이 힌트주고 각자 코드에 맞게 알아서 적용해보기

#11111111111111111111111111111111111111111111111111111111111111111111
# for re in "y":
def numberGame():
    print('---------------------------게임하자 -----------------------')
    numberGame.counter +=1
    #7
    print('{}번쩨 게임중~'.format(numberGame.counter))
    #2
    fir, sec = list(map(int, input('범위를 설정해 주세요!: ').split(',')))
    print(fir, sec)
    number = random.randint(fir, sec)
    print(number)
    num =1
    
    #1
    maxm = int(input("시도 가능 횟수:"))
    while maxm>0: 
            maxm -=1
            guess = int(input('숫자입력:'))
            #8
            score = 110-num*10
            if guess == number:
                print('---------------------------')
                print('정답입니다')
                print('점수는', score ,'점입니다 ')
                print('good job {} 번만에 성공'.format(num))
                #3
                re = (input('다시 해볼래? y/n'))
                while(re != "y" and re != "n" and re != "Y" and re !="N"):
                    print('y or n')
                    re = (input('다시 해볼래? y/n'))
                    if re =="y":
                        numberGame()
                    else:
                        sys.exit(1)
                if re =="y":
                    numberGame()
                else:
                     sys.exit(1)
                break
            #4 #5
            elif guess > number and guess <= sec:
                print('더 작은 수 입니다{}번 남음'.format(max)) 
                num+=1
            elif guess < number and guess >=fir:
                print('더 큰 수 입니다{}번 남음'.format(max))
                num+=1
            else:
                print('범위안에 입력해라 숫자{}~{},{}번남음 '.format(fir,sec,max))
                num+=1
            

    print('게임 오버')
    re = (input('다시 해볼래? y/n'))
    while(re != "y" and re != "n" and re != "Y" and re !="N"):
            print('y or n')
            re = (input('다시 해볼래? y/n'))
            if re =="y":
                numberGame()
            else:
                #6
                sys.exit(1)
    if re =="y":
        numberGame()
    else:
        sys.exit(1)    
numberGame.counter =0    
numberGame()

#2222222222222222222222222222222222222222222222222222222222222222222
import sys
import random
computerlose = random.randint(1,3)
def number(num):
    nums = str(num)
    ct = nums.count('3') + nums.count('6') + nums.count('9')
    if ct:
        return '짝'*ct
    return nums

num = 1

#멀티 플레이어
play_num = int(input('컴퓨터 플레이어 숫자 입력:'))
play_muilty = int(input('멀티 플레이어 수'))
# def game369():
while True:
    for i in range(1,play_num+1):
        ans = number(num)
        print("{}번 플레이어: {}".format(i, ans))
        num +=1
        
    for i in range(1,play_muilty+1):
        i = input("{} turn:".format(i))
        if number(num)!= i:
            print("패배")
            sys.exit(1)
            break
        num +=1


#33333333333333333333333333333333333333333333333
import random
import string


## 지정된 단어
answer = 'orange'
show = '_' * len(answer)
alphabets = []
##꺼내쓰기
# wordList = ['soju', 'notebook', 'study', 'original', 'sessions'] 
# def getWord():
#     return wordList[random.randint(0,len(wordList)-1)]
# print(getWord())

## 랜덤 문자열
# s = string.ascii_lowercase
# re=''
# lenth = int(input("문자의 길이를 입력하세요 : "))
# for i in range(lenth):
#     re += random.choice(s)
#print(re)

while True:
    origin = []

    print("+++++++++++++++++++++++++++++++++++++")
    while True:
        guess = input("알파벳???: ")
        if guess in alphabets:
            print("이미 시도함")
        else:
            break

    alphabets.append(guess)

    for i in range(len(answer)):
        if answer[i] == guess:
            origin.append(i)

    if origin == []:
        print("아무것도 없네요~")
    else:
        show_list = list(show)
        for index in origin:
            show_list[index] = guess
        show = "".join(show_list)
        if not ('_' in show):
            print(answer)
            print("다 맞췄당~!")
            break



#44444444444444444444444444444444444444

import sys
from random import *

#1 시도횟수
#2 다시하기  
#3,4,5,6,7,8 과제 1에서 했던것들 

def baseballGame():

    #랜덤
    num_li=[1,2,3,4,5,6,7,8,9]
    answer =''
    for i in range(3):
        answer += str(num_li.pop(randint(1,len(num_li)-1)))
    print(answer)
    #꺼내쓰기
    # strikenum = [123, 456, 789, 912, 234] 
    # def getnum():
    #     return strikenum[random.randint(0,len(strikenum)-1)]
    
    # getstrike=getnum()
    print(answer)
    print('-----------------야구게임 시작----------')
    gamechance = int(input('몇번 시도?'))
    while gamechance >0:
        gamechance -=1
        strike = 0
        ball = 0
        guess = (input("숫자3개 입력해주세요: "))
        if len(answer) != len(guess):
            guess = (input("숫자3개 입력해주세요: "))
            continue

        for i in range(3):
            if guess[i] == answer[i]:
                strike += 1
            if (guess[i] in answer) & (guess[i] != answer[i]):
                ball +=1
        if (strike == 0) & (ball == 0):
            print("아웃!")
        else:
            if strike == 3:
                print("3스트라이크 ")
                break
            else:
               print(" {} 스트라이크 {}볼!".format(strike,ball))    
    print('game over')
    re = (input('다시 해볼래? y/n'))
    while(re != "y" and re != "n" and re != "Y" and re !="N"):
        print('y or n')
        re = (input('다시 해볼래? y/n'))
        if re =="y":
            baseballGame()
        else:
            sys.exit(1)
    if re =="y":
        baseballGame()
    else:
        sys.exit(1)  
    
baseballGame()

