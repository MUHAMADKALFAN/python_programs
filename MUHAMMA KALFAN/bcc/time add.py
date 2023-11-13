class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addtime(self, other_time):
        total_minutes = (self.hours + other_time.hours) * 60 + (self.minutes + other_time.minutes)
        new_hours = total_minutes // 60 
        new_minutes = total_minutes % 60
        return Time(new_hours, new_minutes)

    def displaytime(self):
        print(f"{self.hours} hr and {self.minutes} min")

    def displayMinutes(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"{total_minutes} minute")

time1=Time(2,50)
time2=Time(1,20)

sum_time = time1.addtime(time2)

sum_time.displaytime()  
sum_time.displayMinutes() 
