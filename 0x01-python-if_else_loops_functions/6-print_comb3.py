#!/usr/bin/python3
for i in  range (0, 9):
    for j in range (i+1, 10):
        if int(str(i) + str(j)) < 89:
            print("{}{}".format(i, j), end=", ")
        else:
            print(89)
