#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    counter = 0
    primary_diagonal = []
    for i in arr:
        primary_diagonal.append(i[counter])
        counter += 1
    counter = len(arr) - 1
    secondary_diagonal = []
    for i in arr:
        secondary_diagonal.append(i[counter])
        counter -= 1
    pri_sum = sum(primary_diagonal)
    sec_sum = sum(secondary_diagonal)
    return abs(pri_sum - sec_sum)

if __name__ == '__main__':
    OUTPUT_PATH="/Users/jcardillo/Desktop/output.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)
    fptr.write(str(result) + '\n')
    fptr.close()
