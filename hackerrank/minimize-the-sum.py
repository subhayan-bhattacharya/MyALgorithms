# https://www.hackerrank.com/contests/101hack55/challenges/minimize-the-sum
# https://www.youtube.com/watch?v=xonmFdwR-Ew&feature=youtu.be
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSum function below.
def minimumSum(l, r):
    # Return the minimum sum among all arrays that satisfy the condition.
    a = l[0]
    b = r[0]
    total = 0
    end = len(l) - 1
    for i in range(1,end + 1):
        c = l[i]
        d = r[i]
        #The previous lowest is more than the next highest
        if a > d:
            total = total + abs(d - a)
            a = d
            b = d
        #The previous highest is less than the next lowest
        elif c > b:
            total = total + abs(c - b)
            a = c
            b = c
        else:
            #There is an overlap
            if c > a:
                a = c
            if d < b:
                b = d
    return total
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    l = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = minimumSum(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
