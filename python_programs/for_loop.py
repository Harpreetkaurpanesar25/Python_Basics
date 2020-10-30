#!/usr/bin/python3

#user input
number =int(input())
for i in range(1, 5):
    mul_table = number * i
    print("{} * {} = {}".format(number, i, mul_table))
