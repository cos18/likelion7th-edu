# 행맨
import random
# answers = ["hello", "howareyou", "imfinethankyou", "banana"]
# ans = random.choice(answers)
def printProgress(p):
    for a in p:
        print(a, end="")
    print()
ans = "tomorrow"
progress = ["_", " "]*len(ans)
while True:
    printProgress(progress)
    inp = input("글자를 입력하세요")
    if inp in ans:
        loc = -1
        tmp = ans
        while True:
            if not inp in tmp:
                break
            loc = loc + tmp.index(inp) + 1
            progress[2*loc] = inp
            tmp = tmp[tmp.index(inp)+1:]
            
    if not '_' in progress:
        printProgress(progress)
        break
    
