class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_int(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    @classmethod
    def int_to_time(cls, seconds):
        new_time = Time()
        (minutes, new_time.second) = divmod(seconds, 60)
        (new_time.hour, new_time.minute) = divmod(minutes, 60)
        return new_time

    def add_time(self, other):
        return Time.int_to_time(self.time_to_int() + other.time_to_int())

    def increment(self, seconds):
        return Time.int_to_time(self.time_to_int() + seconds)

    def __str__(self):
        return "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)


t = Time(9, 10, 11)
t1 = Time(11, 12, 13)
x = vars(t)
print(x["hour"])
