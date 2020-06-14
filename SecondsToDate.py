# Write a Python program to convert seconds to day, hour, minutes and seconds.

from datetime import timedelta


def sec_to_hms(seconds):
    hours = seconds // 3600
    seconds = seconds - hours * 3600
    minutes = seconds // 60
    seconds = seconds - minutes * 60
    return f'{hours}:{minutes}:{seconds}'


time = timedelta(seconds=1012100)

# print(sec_to_hms(10121))
print(time)

# TODO Use datetime library to solve problem Seconds to Date
