#!/bin/python3

import math
# https://www.hackerrank.com/challenges/fair-rations/problem

import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    start = 0
    end = len(B) - 1
    total = 0
    total = 0
    while start <= end - 1:
        if B[start] % 2 != 0:
            B[start] = B[start] + 1
            B[start+1] = B[start+1] + 1
            total = total + 2
        start = start + 1
    if B[end - 1] % 2 == 0:
        if B[end] % 2 != 0:
            return "NO"

    return total
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
    
if __name__ == '__main__':
    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)
    
    print (result)