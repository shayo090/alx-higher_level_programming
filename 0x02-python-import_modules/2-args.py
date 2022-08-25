#!/usr/bin/python3
import sys

if __name__ == '__main__':
    
    av = sys.argv
    ac = len(av) - 1

    if ac > 1:
        print(ac, 'arguments:')
        for i in range(1, ac + 1):
            print('{:d}: {}'.format(i, av[i]))
    elif ac == 1:
        print(ac, 'argument:')
        for i in range(1, ac + 1):
            print('{:d}: {}'.format(i, av[i]))
    elif ac == 0:
        print(ac, 'arguments.')
