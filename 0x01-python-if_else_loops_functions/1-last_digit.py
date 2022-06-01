#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    l_digit = number % 10
else:
    l_digit = number % -10

if l_digit > 5:
    print("Last digit of {} is {}".format(number, l_digit),"and is greater than 5")
elif l_digit == 0:
    print("Last digit of {} is {}".format(number, l_digit),"and is 0")
else:
    print("Last digit of {} is {}".format(number, l_digit),"and is less than 6 and not 0")
