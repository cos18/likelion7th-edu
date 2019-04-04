import getpass
from random import *

#서론

print("\n행맨 게임입니다. 7개의 목숨이 다하면 행맨이 죽습니다 ㅜㅜ")
print("\n지혜로운 그대여, 행맨을 구해주세요! ")
print("(완전한 정답을 알겠다면 알파벳이 아닌 단어를 통째로 적어주세요)\n")

incorrect_cnt = 0
stopper = 0

# 2. 일정 횟수 다하면 행맨 죽이기  3. 모습 출력하기  
HANGMANPICS = ['''
life : 7 
  
     
      
      
      
      
=========''', '''
life : 6  
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
life : 5
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
life : 4
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
life : 3
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
life : 2
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
life : 1
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
 띠로리~~			
  +---+
  |   |
  O   |
 /|\  |	  GAME OVER
 / \  |
      |
=========''']
#[출처] [Python-game]HANGMAN|작성자 skyfort  + 아주 약간의 수정



# 1. 여러 단어 중 랜덤으로 뽑아 맞추기  5. 바구니에 넣을 단어 직접 입력하기

word_num = int(input("문제 바구니에 몇 개의 단어를 넣으시겠습니까? : ") )
word_basket = [30 for i in range(word_num)]
for i in range(word_num):
	word_basket[i] = getpass.getpass("단어를 입력해 주세요 : ")
	
answer = str(word_basket.pop( randint(0, word_num-1  )  ) )

#answer = 'likelion'

show = '_' * len(answer)
deadalphabets = []

while True:
	indexli = []
	if incorrect_cnt == 7 or stopper == 1:
		break
	else:
		#if incorrect_cnt != 0 :
		print(HANGMANPICS[incorrect_cnt])
		print("=================================\n"+show+"\n")

		
		while True:
			if (incorrect_cnt == 7):
				break
			else:	
				guess = input("\n알파벳 or 정답을 적어주세요: ")
				# 4. 답 통째로 맞추면 한 번에 끝내기
				if guess == answer:
					print("\n")
					print(answer)
					print("\n이런...한 번에 맞추다니..")
					print("님 좀 짱인듯 >.<!")
					stopper = 1
					break
				else:
					if guess in deadalphabets:
						print("\n이미 시도한 입력값입니다.")
						incorrect_cnt +=1
						print(HANGMANPICS[incorrect_cnt])	
						print("=================================\n"+show+"\n")
						
					else:
						break
			
				
		deadalphabets.append(guess)
		
		for i in range(len(answer)):
			if answer[i] == guess:
				indexli.append(i)
		
		if (indexli == []) & (incorrect_cnt < 7) & (guess != answer):
			
			print("\n아무것도 없네요~")
			incorrect_cnt += 1
			if incorrect_cnt == 7:	
				print(HANGMANPICS[incorrect_cnt])	
				print("=================================\n"+show+"\n")
			
			
		else:
			show_list = list(show)
			for index in indexli:
				show_list[index] = guess	
			show = "".join(show_list)
			if not ('_' in show):
				print(answer)
				print("\n다 맞췄당~!")
				break
			
		
		






