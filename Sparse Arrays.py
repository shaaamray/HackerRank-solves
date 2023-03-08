#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#


def matchingStrings(stringList, queries):
    # Write your code here
    # solving using Dictionary
    word = dict()
    matchNumbers = []
    for i in stringList:
        if i in word:
            word[i] += 1  # increasing the index number as value again
        else:
            word[i] = 1  # index set to 1 as new value

    for j in queries:
        if j in word:
            # if value matches; sending the app num
            matchNumbers.append(word[j])
        else:
            matchNumbers.append(0)  # if no value in stringList; sending 0

    return matchNumbers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
