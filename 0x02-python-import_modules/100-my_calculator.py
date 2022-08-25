#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':

    argc = len(argv) - 1

    if argc == 3:
        operator = argv[2]
        a = int(argv[1])
        b = int(argv[3])

        if operator == '+':
            result = add(a, b)
            print('{:d} + {:d} = {:d}'.format(a, b, result))
            exit(0)

        elif operator == '-':
            result = sub(a, b)
            print('{:d} - {:d} = {:d}'.format(a, b, result))
            exit(0)

        elif operator == '*':
            result = mul(a, b)
            print('{:d} * {:d} = {:d}'.format(a, b, result))
            exit(0)

        elif operator == '/':
            res = div(a, b)
            print('{:d} / {:d} = {:d}'.format(a, b, result))
            exit(0)

        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
