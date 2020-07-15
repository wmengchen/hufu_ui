class Time():
    def __init__(self,sec):
        self.sec = sec
    @staticmethod
    def sec_minutes(s1,s2):
        return abs(s1-s2)

s = Time(10)
print(Time.sec_minutes(10,5),s.sec_minutes(s.sec,5))
