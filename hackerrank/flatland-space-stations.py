# https://www.hackerrank.com/challenges/flatland-space-stations/problem

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    stations = sorted(c)
    cities = [i for i in range(n)]
    start = 0
    end = len(stations) - 1
    distance = 0
    for c in cities:
        nearest_dist = 0
        if c <= stations[start]:
            nearest_dist = stations[start] - c
        elif c >= stations[end]:
            nearest_dist = c - stations[end]
        else:
            flag = False
            while flag is not True:
                if c == stations[start]:
                    nearest_dist = 0
                    flag = True
                elif c > stations[start]:
                    if stations[start+1] > c:
                        nearest_dist = min(c - stations[start],stations[start + 1] - c)
                        flag = True
                if not flag:
                    start = start + 1
        distance = max(distance,nearest_dist)
    return distance
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
