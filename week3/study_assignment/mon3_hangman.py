import random

# 행맨 모습 출력
hangmanpic = ["""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ HELP
|   |   
|   | 
|  | 
|  | 
|
--------
""",
""""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
"""
 ]

def show_part(your_answer, answer, character):
    for i in range(0, len(answer)):
        if answer[i] == character:
            your_answer = your_answer[:i] + character + your_answer[i+1:]

    return your_answer


#여러 단어가 랜덤으로 출제되게 만드세요.
word_list = ["likelion", "quick", "brown", "fox", "jumps", "over", "lazy", "dog"]

number = random.randrange(0, len(word_list)-1)
answer = word_list[number]
your_answer = "_" * len(word_list[number])

#목숨을 만들어 일정 횟수 이상 틀리면 행맨이 죽게 해주세요
chances = 9
print("Guess your word! The length of the word is: ", len(word_list[number]))

while True:
    print("======================")
    print("You got " + str(chances) + "chances left!!!")
    print('Your status: ' + your_answer)
    print("======================")
    print(hangmanpic[9-chances]) #행맨 그림 출력하기

    character = input("Choose your character(or if you can guess the whole word, say it!): ")

    #단어 자체를 알겠으면 아예 맞추는 기능
    if character == answer:
        your_answer = character
        print("Well, you got the answer itself!")
    elif character in answer:
        print("You got part of it right!")
        your_answer = show_part(your_answer, answer, character)
    else:
        print("Wrong! Pick another!")
        chances -= 1
    
    if(your_answer == answer):
        print("You win! The answer was: ", answer)
        break

    if(chances == 0):
        print("Haha! You suck! The real answer was: ", answer)

        retry = input("Would you like to try another game~? (y/n): ")
        if(retry == 'n'):
            print("Alright, game over then!")
            break
        elif(retry == 'y'):
            #게임 초기화
            chances = 9
            number = random.randrange(0, len(word_list)-1)
            answer = word_list[number]
            your_answer = "_" * len(word_list[number])
            print("ANOTHER GAME NOW!\n\n\n\n\n\n\n\n\n")
        else:
            print("nope")

print("This is the end of this game.")

