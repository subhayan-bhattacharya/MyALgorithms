#https://www.hackerrank.com/challenges/maximum-element/problem

stack = []
maxstack = []
testcases = int(input())
for i in range(testcases):
    line = list(map(int,input().split(' ')))
    if len(line) == 2:
        stack.append(line[1])
        if len(maxstack) == 0:
            maxstack.append(line[1])
        else:
            if line[1] >= maxstack[-1]:
                maxstack.append(line[1])
    elif line[0] == 2:
        elem = stack[-1]
        del stack[-1]
        if elem == maxstack[-1]:
            del maxstack[-1]
    else:
        print (maxstack[-1])
        