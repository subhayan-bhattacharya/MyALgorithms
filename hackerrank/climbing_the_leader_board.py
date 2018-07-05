# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def find_ceil(arr,start,end,element):
    if arr[start] > element:
        return start
    if arr[end] < element:
        return -1
    
    mid = int(start + (end - start)/2)
    if arr[mid] == element:
        return mid
    elif arr[mid] > element:
        if arr[mid-1] < element:
            return mid
        elif arr[mid -1] == element:
            return mid -1
        else:
            return find_ceil(arr,start,mid - 1,element)
    else:
        if arr[mid + 1] >= element:
            return mid +1
        else:
            return find_ceil(arr,mid+1,end,element)

def climbingLeaderboard(scores, alice):
    ranks = []
    sorted_scores = sorted(set(scores))
    for score in alice:
        pos = find_ceil(sorted_scores,0,len(sorted_scores) - 1,score)
        if sorted_scores[pos] == score:
            ranks.append(len(sorted_scores) - pos)
        elif pos == -1:
            ranks.append(1)
        else:
            ranks.append(len(sorted_scores) - pos + 1)
    return ranks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
