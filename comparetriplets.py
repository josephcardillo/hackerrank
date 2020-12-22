#!/bin/python3

import math
import os
import random
import re
import sys
import itertools


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    output = []
    alice_points = 0
    bob_points = 0
    for (num1, num2) in zip(a, b):
        if num1 > num2:
            alice_points += 1
        elif num1 < num2:
            bob_points += 1
        else:
            continue
    output.append(alice_points)
    output.append(bob_points)
    return output

if __name__ == '__main__':
    OUTPUT_PATH="/Users/jcardillo/Desktop/output.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    print(result)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()