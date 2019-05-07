# 369

def checkjjak(i):
    while i>=1:
        if(i%10%3==0):
            return True
        i /= 10
        i = int(i)
    return False

ans = 1
while True:
    inp = input("입력하세요 : ")
    if (not checkjjak(ans)) and str(ans) != inp:
        print("틀렸습니다")
        break
    ans += 1
