# https://www.hackerrank.com/challenges/balanced-brackets
tests = int(input())
for i in range(tests):
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
            if len(track) == 0:
                negative = 1
                break
            if c != matches[track[-1]]:
                negative = 1
                break
            else:
                del track[-1]
    if negative == 1: 
        print ("NO")
    else:
        if len(track) > 0:
            print ("NO")
        else:
            print ("YES")