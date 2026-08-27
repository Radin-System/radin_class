# function -> Tabe
"""
print()
len()
sum()
round()
input()
"""

def average(numbers, float_digits = 2):
    for number in numbers:
        if number > 20 or number < 0:
            print('Error: numbers should be between 0-20')
            return 'Error'

    result = round(sum(numbers) / len(numbers), float_digits)
    return result


avg = average((19, 18, 20, 17, 14, 13), float_digits = 3)
print(f'Mohammad AVG: {avg}')


import os
import platform
import time
import threading

print(os.name)
print(platform.platform())
