from threading import Timer
from data import Time
from typing import Optional
from data import Point

import data

# Write your functions for each part in the space below.

# Part 3
# This function adds up two given times and returns the sum
# input: two Type objects
# output: one Type object
def time_add(time1: Time, time2: Time) -> Time:
    time3 = Time(hour  = time1.hour + time2.hour,
                 minute = time1.minute + time2.minute,
                 second = time1.second + time2.second)
    if time3.second >= 60:
        time3.minute += (time3.second // 60)
        time3.second %= 60
    if time3.minute >= 60:
        time3.hour += (time3.minute // 60)
        time3.minute %= 60
    return time3

# Part 4
# This functions checks if a list is descending in value
# input: a list of floats
# output: a boolean
def is_descending(list1: list[float]) -> bool:
    for i in range(1, len(list1)):
        if list1[i] >= list1[i - 1]:
            return False
    return True

# Part 5
# This function gives the index of the greatest value in a list between two given indices
# input: one list of integers, two integers
# output: an optional output between integer and None
def largest_between(list1: list[int], lower: int, upper: int) -> Optional[int]:
    if lower > upper or lower < 0 or upper >= len(list1):
        return None
    max_i = lower
    max_value = list1[lower]
    for i in range(lower, upper + 1):
        if list1[i] >= max_value:

            max_value = list1[i]
            max_i = i
    return max_i


# Part 6
def furthest_from_origin(list1: list[Point]) -> int:
    distances = []
    for point in list1:
        distances.append(int(point.x**2 + point.y**2))
    return largest_between(distances, 0, len(distances) - 1)