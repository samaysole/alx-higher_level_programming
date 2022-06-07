#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return
    i = len(my_list) - 1
    max = my_list[0]
    while i > 1:
        j = 0
        while j < i:
            if max < my_list[j]:
                if my_list[j] > my_list[j + 1]:
                    max = my_list[j]
                else:
                    max = my_list[j + 1]
        j += 1
    i -= 1
    return max
