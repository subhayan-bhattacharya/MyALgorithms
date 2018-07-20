# https://www.hackerrank.com/contests/101hack55/challenges/swapping-in-an-array/submissions/code/1308842497

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the swapToSort function below.
def swapToSort(a):
    # Return -1 or 0 or 1 as described in the problem statement.
    sorted_a = sorted(a)
    if sorted_a == a:
        return 0
    start = 0
    end = len(a) - 1
    found = False
    while start < end:
        if a[start] <= a[start + 1]:
            start = start + 1
        else:
            if not found:
                outofplace_index = start
                start = start + 1
                found = True
            else:
                temp = a[outofplace_index]
                a[outofplace_index] = a[start + 1]
                a[start + 1] = temp
                if a == sorted_a:
                    return 1
                else:
                    return -1
    if found:
        return 1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = swapToSort(a)

    fptr.write(str(result) + '\n')

    fptr.close()