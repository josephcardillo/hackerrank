#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    num_of_pos = 0
    num_of_neg = 0
    num_of_zero = 0
    for num in arr:
        if num < 0:
            num_of_neg += 1
        elif num > 0:
            num_of_pos += 1
        else:
            num_of_zero += 1
    print("%6f" % (num_of_pos / n))
    print("%6f" % (num_of_neg / n))
    print("%6f" % (num_of_zero / n))

# Investigate this for later use:
# https://docs.python.org/3/tutorial/inputoutput.html#old-string-formatting

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)