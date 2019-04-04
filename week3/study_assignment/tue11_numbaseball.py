import random
lennumber=int(input('원하는 자릿수를 입력하세요: '))
rangefrom=int(10**(lennumber-1))
rangeto=int((10**lennumber)-1)

while True:
    answer=str(random.randint(rangefrom,rangeto))
    for i in answer:
        if answer.count(i)!=1:
            continue
    break
print(answer)

def updown(n):
    if n<answer:
        print('업!')
    elif n>answer:
        print('다운!')

num=0
number=str()
while number != answer:
    number=str(input ('숫자를 입력해주세요: '))

    countS = 0
    countB = 0
    temp_list = [x for x in answer]     
    for i in range(len(answer)):
        
        if number[i] == temp_list[i]:
            countS = countS + 1
            temp_list[i] = ''
            
        elif number.count(temp_list[i]):
            countB = countB + 1

    if countS == 0 and countB == 0:
        print('아웃!')
        updown(number)
        num+=1
        continue

    print('{} 스트라이크!'.format(countS), '●'*countS,'○'*(len(answer)-countS))
    print('{} 볼!'.format(countB), '●'*countB,'○'*(len(answer)-countB))
    updown(number)
    num+=1



print('정답입니다! {}번만에 맞추셨습니다!'.format(num))

