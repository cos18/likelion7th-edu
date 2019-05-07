# 숫자야구

import random

class Baseball:
    def __init__(self):
        self.ans = ""
        self.result = []
        print("Baseball 클래스 객체 생성")
        
    def setAns(self):
        nums = list(range(1, 10))
        for i in range(3):
            a = random.choice(nums)
            self.ans = self.ans + str(a)
            nums.remove(a)
        print("setAns 함수 완료 : {}".format(self.ans))

    def isThisAns(self, inp):
        strike = 0
        ball = 0
        for i in inp:
            if i in self.ans:
                if inp.index(i) == self.ans.index(i):
                    strike += 1
                else:
                    ball+=1
        print("{} strike {} ball".format(strike, ball))
        self.result.append([inp, [strike, ball]])
        if strike == 3:
            return True
        return False

    def printResult(s):
        for r in s.result:
            print("입력값 : {} / 결과 : {}S{}B".format(r[0], r[1][0], r[1][1]))

game = Baseball()
game.setAns()
while True:
    inp = input("입력하세요 :")
    if(game.isThisAns(inp)):
        break

game.printResult()

'''
while True:
    strike = 0
    ball = 0
    inp = input("입력하세요 :")
    for i in inp:
        if i in ans:
            if inp.index(i) == ans.index(i):
                strike += 1
            else:
                ball+=1
    print("{} strike {} ball".format(strike, ball))
    if strike == 3:
        break
'''
