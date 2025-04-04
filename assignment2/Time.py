class time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def addTime(self,t1,t2):
        totalMinutes=t1.minutes + t2.minutes
        totalHours=t1.hours + t2.hours + totalMinutes//60
        totalMinutes=totalMinutes % 60
        self.hours=totalHours
        self.minutes=totalMinutes
    def showTime(self):
        print(f"Time: {self.hours}hrs {self.minutes}mins") 
    def showMinute(self):
        print(f"Total Minutes:{self.minutes+self.hours*60}")
t1=time(1,50)  
t2=time(2,40)        
t1.addTime(t1,t2)
t1.showTime()
t1.showMinute()           


        
