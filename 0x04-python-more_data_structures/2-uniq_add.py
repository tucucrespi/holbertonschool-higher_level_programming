#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniq_numbers = set(my_list)
    for num in uniq_numbers:
        sum += num
    return sum
