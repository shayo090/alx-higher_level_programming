#!/usr/bin/python3

def multiple_returns(sentence):
    len_s = len(sentence)
    first_c = sentence[0]
    if len_s == "":
        return (len_s, None)
    return (len_s, first_c)
