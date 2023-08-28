import time
import math
import datetime


def time_in_googol():
    time_since_unix_minutes = math.floor(time.time() // 60)
    print(time_since_unix_minutes)
    googol = 10**100
    time_in_googol_minutes = time_since_unix_minutes + googol
    print(time_in_googol_minutes)
    print(datetime.datetime.fromtimestamp(time_in_googol_minutes))


time_in_googol()
