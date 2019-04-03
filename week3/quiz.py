alpha = ['A', 'B', 'C']
# 게임 판은 이차원 리스트를 사용한다.
pan = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
# pan = [['O', 'O', 'O'],['O', 'O', 'O'],['O', 'O', 'O']]
turn = 'O'
count = 0
win = ' '
print("====> Tic Tac Toe <====")
print()
# 끝날 때 까지 계속 반복한다.
while True:
    # 1. 판을 출력한다.
    print('==============')
    print('    1   2   3')
    for l in range(3):
        print(' {}  '.format(alpha[l]), end="")
        for c in range(3):
            print(pan[l][c], "", end="")
            if(c!=2):
                print("| ", end="")
        print()
        if(l!=2):
            print('   -----------')
    print('==============')
    # 2. 사용자가 차지할 칸을 입력받는다.
    select = input("{}의 차례입니다 >> ".format(turn)) # 입력형식 : A2, B3 요런식으로
    # 3. 입력받은 값이 잘못되었는지 확인하면서 어디 칸인지 저장한다.
    try:
        row = alpha.index(select[0]) # 3-1. 첫글자에 입력한 글자가 A~C안에 들어갔는지 확인한다
    except:
        print('잘못 입력하셨습니다. 다시 입력해주세요.')
        continue
    try:
        collum = int(select[1])-1 # 3-2. 두번째에 입력한 글자가 정수인지 확인한다.
    except:
        print('잘못 입력하셨습니다. 다시 입력해주세요.')
        continue
    if(collum<0 or collum>2): # 3-3. 두번째에 입력한 글자가 1~3안에 들어가는지 확인한다.
        print('잘못 입력하셨습니다. 다시 입력해주세요.')
        continue
    if(pan[row][collum] != ' '): # 3-4. 이미 다른 사람이 차지한 땅인지 확인한다
        print('이미 주인이 있는 칸입니다. 다시 입력해주세요.')
        continue
    # 4. 땅을 차지한다!
    pan[row][collum] = turn 
    # 5. 승리 조건을 확인한다.
    if((pan[0][0] == pan[0][1] and pan[0][1]==pan[0][2]) or (pan[0][0]==pan[1][1] and pan[1][1]==pan[2][2]) or (pan[0][0]==pan[1][0] and pan[1][0]==pan[2][0])):
        if(pan[0][0]!=' '): # 5-1. 이때 비교시 빈칸이 같은걸로 판명되지 않게 확인한다.
            win = turn # 5-2. 승리 판별시 승리자를 출력하기 위해 현재 차례 사람을 저장한다.
            break
    if((pan[1][0] == pan[1][1] and pan[1][1]==pan[1][2]) or (pan[0][1]==pan[1][1] and pan[1][1]==pan[2][1]) or (pan[0][2]==pan[1][1] and pan[1][1]==pan[2][0])):
        if(pan[1][1]!=' '):
            win = turn
            break
    if((pan[2][0]==pan[2][1] and pan[2][1]==pan[2][2]) or (pan[0][2]==pan[1][2] and pan[1][2]==pan[2][2])):
        if(pan[2][2]!=' '):
            win = turn
            break
    # 5-3. 무승부를 판단한다
    count += 1
    if(count == 9): # 9번 했다는 것은 모든 판이 채워졌으나 승리조건이 만족되지 않았음으로 비긴 판이다.
        break
    # 6. 차례를 바꾼다.
    if(turn == 'O'):
        turn = 'X'
    else:
        turn = 'O'
print("===============")
print("게임이 끝났습니다!")

# 7. 승패를 출력한다.
if(win==' '): # 7-1. 빈칸인 경우 win변수에 변화가 없음으로 비긴것
    print("비겼습니다...!")
else:
    print("{} 승리!!".format(win))