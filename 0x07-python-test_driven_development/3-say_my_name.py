#!/usr/bin/python3

"""
function that prints
first_name and last_name must be strings otherwise, raise a TypeError exception
with the message first_name must be a string or last_name must be a string
"""


def say_my_name(first_name, last_name=""):

    """
    prints My name is <first name> <last name>
    """

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print("My name is {:s} {:s}".format(first_name, last_name))
