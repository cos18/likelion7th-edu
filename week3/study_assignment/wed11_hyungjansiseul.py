#행맨
from random import * 

answer_list =['mother', 'father', 'sister', 'brother','yeemo']
answer = choice(answer_list)
print(answer)
hangman_li =[
    '',
    ' o',
    ' o\n |',
    ' o\n/|\\',
    ' o\n/|\\\n/',
    '\n/|\\\n/ \\  ..ㅇ'
]

turn = 'A'
wrong_try = 0
show = '_' * len(answer)
A_try = 0
B_try = 0
tried = []
playing = True
indexli = []
#함수부분
def guess():
    guessing = True
    while guessing:
        input_guess = input("알파벳을 적어주세요: ").lower()
        if input_guess in tried:
            print("이미 시도한 알파벳입니다!")
        else:
            tried.append(input_guess)
            guessing = False
            return input_guess

def check(guess,team):
    global A_try
    global B_try
    global indexli
    global answer
    global show 

    for i in range(len(answer)):
        if answer[i] == guess:
            indexli.append(i)

    if indexli == []:
        print("아무것도 없네요~")
        if team == 'A':
            A_try +=1
        else:
            B_try +=1
    else:
        print("%s개가 있네요!"%len(indexli))
        show_list = list(show)
        for index in indexli:
            show_list[index] = guess
        show = "".join(show_list)
    
def correct_check(team):
    global playing
    if not ('_' in show):
        print(answer)
        print("%s가 이겼습니다!" %team)
        playing = False

def dead_check(team, team_try):
    global playing
    if team_try == 5:
        print("%s는 형장의 이슬로 사라졌습니다..." %team)
        
        playing = False
            
    




while playing:
    indexli = []    
    print("==========================\n"+show+"\n")


    

    print("%s팀의 차례입니다." %turn)
    
    if turn == 'A':
        A_guess = guess()
        check(A_guess,turn)
        correct_check(turn)
        dead_check(turn, A_try)
        print(hangman_li[A_try])
        turn = 'B'
    else:
        B_guess = guess()
        check(B_guess,turn)
        correct_check(turn)
        dead_check(turn, B_try)
        print(hangman_li[B_try])
        turn = 'A'

