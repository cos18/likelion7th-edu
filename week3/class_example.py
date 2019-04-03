# 세션 전 미리 준비한 파일
class WasherFactory:
    machineName = "세탁기"
    def __init__(self, washerType):
        self.washerType = washerType

    def wash(self, time):
        print("{} 타입의 새탁기를 {}분동안 돌립니다~~".format(self.washerType, time))
        # 세탁기를 돌린다.

    def dry(self, time, howMuch):
        print("{}분동안 {} 건조합니다!!".format(time, howMuch))
        return "성공!"

    def sayYourName(self):
        print("나는 {}에요!".format(self.machineName))

drum = WasherFactory("드럼")
drum.sayYourName()
drum.wash(10)
drum.dry(10, '강력하게!!!')

tong = WasherFactory("통돌이")
tong.sayYourName()
tong.wash(30)
print(tong.dry(20, "잔잔하게...ㅎ"))