#!/bin/python3
# https://www.hackerrank.com/challenges/equal-stacks

n1, n2, n3 = map(int, input().split())
H1 = list(map(int, input().split()))
H2 = list(map(int, input().split()))
H3 = list(map(int, input().split()))

sum_h1 = sum(H1)
sum_h2 = sum(H2)
sum_h3 = sum(H3)
#print (sum_h1,sum_h2,sum_h3)
d1 = 0
d2 = 0
d3 = 0

#Pay attention to the logic of the or part in the below logic(it cannot be and)

while not (sum_h1 == sum_h2 and sum_h2 == sum_h3):
    if d1 == n1 or d2 == n2 or d3 == n3:
        sum_h1 = 0
    if sum_h1 > sum_h2 or sum_h1 > sum_h3:
        sum_h1 -= H1[d1]
        d1 = d1 + 1
    if sum_h2 > sum_h1 or sum_h2 > sum_h3:
        sum_h2 -= H2[d2]
        d2 = d2 + 1
    if sum_h3 > sum_h1 or sum_h3 > sum_h2:
        sum_h3 -= H3[d3]
        d3 = d3 + 1
         
print (sum_h1)