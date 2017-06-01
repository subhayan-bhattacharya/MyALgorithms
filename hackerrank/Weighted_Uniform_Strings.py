#Uniform substrings of abccddde are
'''a b c cc d dd ddd e'''
#https://www.hackerrank.com/challenges/weighted-uniform-string

import string
alphabets = list(string.ascii_lowercase)
d1 = {n:x+1 for x,n in enumerate(alphabets)}

str1 = input()
attempts = int(input()) 
count = 0
prev = ""
weights = set()
for c in str1:
    if c == prev:
        count = count + 1
    else:
        count = 1
        prev = c
    weights.add(count * d1[c])
      
     
for i in range(attempts):
    check = int(input())
    if check in weights:
        print ("Yes")
    else:
        print ("No")
