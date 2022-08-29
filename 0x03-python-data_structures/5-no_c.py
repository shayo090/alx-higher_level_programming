#!/usr/bin/python3

def no_c(my_string):
    new_s = ""
    for i in my_string:
        if i not in 'cC':
            new_s = new_s + i
    return (new_s)
