#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    combos = list(combinations(arr, 4))
    combo_sums = []
    for combo in combos:
        combo_sums.append(sum(combo))
    print(min(combo_sums), max(combo_sums))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)