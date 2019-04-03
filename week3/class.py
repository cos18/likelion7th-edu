# 세션에서 진행한 파일
class WasherFactory():
    machineName = "세탁기"
    def __init__(self, t, voltage): 
        self.t = t # 타입
        self.voltage = voltage

    def wash(self, time):
        print("{} {}를 돌립니다!!!!".format(self.t, self.machineName))
        print("{}분동안 돌립니다!!".format(time))
        self.voltage += 10

    def checkVoltage(self):
        return self.voltage

tongdonlE = WasherFactory("통돌이", 100)
tongdonlE.wash(10)

drum = WasherFactory("드럼", 200)
drum.wash(30)
drum.wash(30)
drum.wash(30)
print(drum.checkVoltage())
print(tongdonlE.checkVoltage())