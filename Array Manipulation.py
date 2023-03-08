#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def arrayManipulation(n, queries):
    # Write your code here
    # will use preFixSum algorithm
    array = [0] * (n+1)

    for i in queries:
        a = i[0]
        b = i[1]
        k = i[2]
        array[a] += k
        if (b+1) <= n:  # (n+1)
            array[b+1] -= k

    maxValue = 0
    currentValue = 0
    for i in range(1, n+1):
        currentValue = currentValue + array[i]
        if currentValue > maxValue:
            maxValue = currentValue
    return maxValue


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
