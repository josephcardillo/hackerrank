#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_hit_count = 0
    orange_hit_count = 0
    for i in range(len(apples)):
        if (s <= a + apples[i] <= t):
            apple_hit_count += 1
    for i in range(len(oranges)):
        if (s <= b + oranges[i] <= t):
            orange_hit_count += 1
    return apple_hit_count, orange_hit_count

if __name__ == '__main__':
    st = input().split()

    s = int(st[0]) # starting point of sam's house

    t = int(st[1]) # ending location of sam's house

    ab = input().split() 

    a = int(ab[0]) # location of apple tree

    b = int(ab[1]) # location of orange tree

    mn = input().split()

    m = int(mn[0]) # number of apples

    n = int(mn[1]) # numer of oranges

    apples = list(map(int, input().rstrip().split())) # array with distances

    oranges = list(map(int, input().rstrip().split())) # array with distances

    apple_count, orange_count = countApplesAndOranges(s, t, a, b, apples, oranges)

    print(apple_count)
    print(orange_count)