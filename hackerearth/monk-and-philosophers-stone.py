# https://www.hackerearth.com/challenge/competitive/codemonk-stacks-queues-1/algorithm/monk-and-philosophers-stone/

number = int(input())
worth = list(map(int,input().split(' ')))
q,x = input().split(' ')
stack = []
monk = 0
to_break = False
start = 0
for i in range(int(q)):
    instruction = input()
    if instruction == "Harry":
        stack.append(worth[start])
        monk = monk + worth[start]
        start = start + 1
        if monk == int(x):
            to_break = True
            break
    elif instruction == "Remove":
        monk = monk - stack[-1]
        del stack[-1]
        if monk == int(x):
            to_break = True
            break
if to_break:
    print (len(stack))
else:
    print (-1)