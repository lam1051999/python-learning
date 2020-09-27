class Time:
    """Represents the time of day.
    Attributes: hour, minute, second"""


# ----------------common------------------
# pure functions


def print_time(t):
    print("The hour is: %.2d" % t.hour)
    print("The minute is: %.2d" % t.minute)
    print("The second is: %.2d" % t.second)


def time_to_int(t):
    seconds = t.hour * 3600 + t.minute * 60 + t.second
    return seconds


def int_to_time(s):
    time = Time()
    time.second = s % 60
    time.minute = ((s - time.second)/60) % 60
    time.hour = (((s - time.second)/60) - time.minute)/60
    return time
# modifiers


def convert_time(t):
    if t.second >= 60:
        t.minute, t.second = t.minute + (t.second // 60), t.second % 60
    if t.minute >= 60:
        t.hour, t.minute = t.hour + (t.minute // 60), t.minute % 60
    if t.hour >= 24:
        t.hour -= 24
# ----------------common------------------

# pure functions


def add_time(t1, t2):
    sum = time_to_int(t1) + time_to_int(t2)
    return int_to_time(sum)

# modifiers


def increment_time(t, seconds):
    t.second += seconds
    convert_time(t)


# main executing
start = Time()
start.hour = 9
start.minute = 8
start.second = 7
duration = Time()
duration.hour = 11
duration.minute = 30
duration.second = 6

total = add_time(start, duration)
increment_time(total, 55)
total_sec = time_to_int(total)
print("Time to int: " + str(total_sec))
total_origin = int_to_time(total_sec)
print_time(total_origin)
