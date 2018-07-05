import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):
    first = set(list(arr[0]))
    count = 0
    for s in first:
        to_break = False
        for a in arr[1:]:
            if s not in a:
                to_break = True
                break
        if not to_break:
            count = count + 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
