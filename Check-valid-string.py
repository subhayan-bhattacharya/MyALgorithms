''' Check if a string has valid starting and ending brackets'''
''' Example : [(a+b)+b] should return True and [(a+b}+b] should return false'''

str1 = input()
matches = {'(':')','[':']','{':'}'}
open = ['(','[','{']
close = [')',']','}']
track = []
negative = 0
for c in str1:
    if c in open:
        track.append(c)
    elif c in close:
        if c != matches[track[-1]]:
            negative = 1
            break
        else:
            del track[-1]
if negative == 1: 
    print ("False")
else:
    print ("True")