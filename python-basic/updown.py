# 업다운
import random
answer = random.randint(1, 100)

while True:
    inp = int(input("입력하세요 : "))
    if inp == answer:
        print("맞췄습니다")
        break
    if inp > answer:
        print("정답보다 큽니다")
    else:
        print("정답보다 작습니다")
