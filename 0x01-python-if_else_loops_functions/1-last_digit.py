#!/usr/bin/python3
import random
number = random.randint(-10000, 1000)
digit = abs(number) % 10
if digit > 5 and number > 0:
    print(f"Last digit of {number} is {digit} and greater than 5")
elif digit == 0:
    print(f"Last digit of {number} is {digit} and 0")
elif digit < 6 and number < 0:
    digit = -digit
    print(f"Last digit of {number} is {digit} and less than 6 and not 0")



