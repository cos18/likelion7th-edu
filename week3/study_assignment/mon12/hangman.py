import random
from tkinter import*

word_list = ["likelion", "skku", "computer", "host", "client", "education", "data", "hangman"]
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ans = word_list[random.randint(0,2)]

#print(ans)

user_ans = []
flag = 1
u_chance = 0

print("행맨 게임 시작")
chance = int(input("행맨의 목숨을 지정해주세요(최소 10번) : "))
print("======================")

for i in range(len(ans)):
    user_ans.append("_")
size = len(ans)
while(flag):

    if chance > u_chance:
        for i in range(size):
            print("%s " %(user_ans[i]), end= '')

        print("\n")


        text = '정답을 맞춰보세요 : '
        guess = input(text)

        if guess in user_ans:
            print("%s는 이미 추측" %(guess))
        
        elif len(guess) == len(ans):
            user_ans.append(guess)
            if guess == ans:
                print("정답을 맞추었습니다.")
                flag = 0
                break
            else:
                print("다시 추측")
                u_chance += 1

        elif len(guess) == 1:
            for i in range(len(ans)):
                if ans[i] == guess:
                    user_ans[i] = ans[i]

            u_chance += 1

        elif guess == "show me hangman":
            window = Tk()
            window.title("현재 행맨 상태")
            window.geometry("1152x648")
            window.resizable(width=TRUE, height = TRUE)


            Hangman_Image = "Hang" + str(u_chance) +".gif"

            if(chance - u_chance == 3):
                Hangman_Image = "Hang7.gif"
            
            if(chance - u_chance == 2):
                Hangman_Image = "Hang8.gif"

            if(chance - u_chance == 1):
                Hangman_Image = "Hang9.gif"
            photo = PhotoImage(file = Hangman_Image)


            label4 = Label(window,image = photo)
            label4.pack()
            window.mainloop()
            #print(Hangman_Image)

    else:
        print("모든 목슴 소진")
        break

if u_chance == chance:
    window = Tk()
    window.title("현재 행맨 상태")
    window.geometry("1152x648")
    window.resizable(width=TRUE, height = TRUE)
    photo = PhotoImage(file = "Hang10.gif")
    label4 = Label(window,image = photo)
    label4.pack()
    window.mainloop()

print("정답 : ")

for i in range(len(ans)):
    print("%s " %(ans[i]), end= '')