#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set_1 = {i for i in set_1 if i not in set_2}
    new_set_2 = {i for i in set_2 if i not in set_1}
    return new_set_1 | new_set_2
