import random

first, second = map(int, input('범위를 설정해 주세요!: ').split())

answer = random.randint(first, second)
life = int(input("횟수를 입력해주세요: "))

while life > 0:
    x = int(input('{} - {}사이의 숫자를 맞춰보세요!: '.format(first, second)))

    if x > second:
        print("범위 초과!")
        
    elif x < answer:
        life -= 1
        print('업!! 남은 횟수는 {}입니다!'.format(life))
        
    elif x > answer:
        life -= 1
        print("다운!! 남은 횟수는 {}입니다!".format(life))
        
    else:
        print("딩동댕!")
        break

'''
구글링=> multiple integer inputs
https://stackoverflow.com/questions/17121706/using-mapint-raw-input-split
'''

#횟수제한
#범위설정
