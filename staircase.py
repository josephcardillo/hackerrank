#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    space = ' '
    pound = '#'
    space_counter = n - 1
    pound_counter = 1
    for i in range(1, n + 1):
        print((space * space_counter) + (pound * pound_counter))
        space_counter -= 1
        pound_counter += 1

if __name__ == '__main__':
    n = int(input())

    staircase(n)