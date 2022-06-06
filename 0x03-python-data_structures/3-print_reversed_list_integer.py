#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    for i in reversed(mylist):
        print("{:d}".format(i))
