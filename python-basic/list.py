# 리스트
# 369 업다운 행맨 숫자야구

# 리스트는 데이터의 모음
a=10
b=20
sungwoo = 80
sangwoo = 70

score = []
score = list()

score = [40, 70, 80, 90, 100]
score = [[40, 40], 50, 70, [90, 80], 80]


# 인덱싱, 슬라이싱
score = [40, 70, 80, 90, 100]
print(score[2])
#print(score[5])
print(score[1:3])
# 이상 , 미만
print(score[:3])
print(score[1:])
big = score*10
print(big)

print("========================")
print("="*20)
print(big[::2])
print(list(range(10)))
# 0이상 *미만
print(list(range(2,10)))
print(list(range(2,100, 10)))


# 더하기, 반복하기, 길이

print(len(score))
score = [[40, 40], 50, 70, [90, 80], 80]
print(len(score))

print("="*20)

a = [1, 2, 3, 4, 2, 3, 1]
print(a.index(3))
for i in range(len(a)):
    if a[i]==3:
        print(i)
print(a.count(3))


print("="*20)
a.append(10)
print(a.pop())


print("="*20)
print(a)
print(sorted(a))
print(a)
a.sort()
print(a)
    
