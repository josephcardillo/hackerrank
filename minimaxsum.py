# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys
# from itertools import combinations

# # Complete the miniMaxSum function below.
# def miniMaxSum(arr):
#     combos = list(combinations(arr, 4)) # https://www.geeksforgeeks.org/python-itertools/
#     combo_sums = []
#     for combo in combos:
#         combo_sums.append(sum(combo))
#     print(min(combo_sums), max(combo_sums))

# if __name__ == '__main__':
#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)

from itertools import combinations

# def find_combos(arr):
#     combos = list(combinations(arr, 4))
#     print(combos)

def find_combos(arr):
    combos = list(combinations(arr, 3))
    print(combos)
    combo_sums = []
    for combo in combos:
        combo_sums.append(sum(combo))
    print(combo_sums)
    print(min(combo_sums), max(combo_sums))

arr = [1, 2, 3, 4, 5]

find_combos(arr)