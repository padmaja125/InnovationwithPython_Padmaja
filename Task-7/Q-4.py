class TotalTime:

    def __init__(self,hour,mins):
        self.hour = hour
        self.mins = mins

    def addTime(t1,t2):
        t3 = TotalTime(0,0)
        t3.hour= t1.hour + t2.hour
        t3.mins = t1.mins + t2.mins
        if t3.mins > 60:
            t3.mins = t3.mins % 60
            t3.hour += 1
        return t3

    def displayTime(self):
        print("total time :", self.hour,self.mins)

    def displayMinute(self):
        print("total minutes :",self.mins + (self.hour *60))

a = TotalTime(2,50)
b = TotalTime(1,20)
c = TotalTime.addTime(a,b)
c.displayTime()
c.displayMinute()