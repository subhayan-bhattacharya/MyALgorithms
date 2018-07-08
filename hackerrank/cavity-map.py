# https://www.hackerrank.com/challenges/cavity-map/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def cavityMap(grid):
    g = list(grid)
    new = []
    for index,s in enumerate(list(g)):
        if index == 0 or index == len(g) - 1:
            new.append(s)
            continue
        else:
            map = list(s)
            for i,key in enumerate(map):
                if i == 0 or i == len(map) - 1:
                    continue
                else:
                    if map[i-1] < key:
                        if map[i+1] < key:
                            if g[index-1][i] < key:
                                if g[index+1][i] < key:
                                    #print ("Changing !!")
                                    map[i] = "X"
        new.append(''.join(map))
    return new

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
