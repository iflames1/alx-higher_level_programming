#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    unsigned_num = number * -1
    unsigned_last_digit = unsigned_num % 10

last_digit = number % 10

if number >= 0:
    if last_digit > 5:
        print("Last digit of {} is {} and is greater than 5".format
              (number, last_digit))
    elif (last_digit < 6 and last_digit != 0):
        print("Last digit of {} is {} and is less than 6 and not 0".format
              (number, last_digit))
    else:
        print("Last digit of {} is {} and is 0".format(number, last_digit))

else:
    if unsigned_last_digit > 5:
        print("Last digit of {} is -{} and is greater than 5".format
              (number, unsigned_last_digit))
    elif (unsigned_last_digit < 6 and unsigned_last_digit != 0):
        print("Last digit of {} is -{} and is less than 6 and not 0".format
              (number, unsigned_last_digit))
    else:
        print("Last digit of {} is {} and is 0".format
              (number, unsigned_last_digit))
