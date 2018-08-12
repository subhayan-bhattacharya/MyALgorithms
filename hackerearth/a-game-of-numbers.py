# https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/a-game-of-numbers-1-5d3a8cb3/description/


from sys import stdin
numbers = int(stdin.readline())
original = []
for i in range(numbers):
    num = int(stdin.readline())
    original.append(num)
greater = [-1] * len(original)
shorter = [-1] * len(original)
stack_1 = []
stack_2 = []

# This for finding out the next greater element in the stack for all elements
for i in range(len(original) - 1, -1, -1):
    while len(stack_1) > 0 and original[stack_1[-1]] <= original[i]:
        stack_1.pop()
        
    if len(stack_1) > 0:
        greater[i] = stack_1[-1]
    else:
        greater[i] = -1
        
    stack_1.append(i)
    
# This for finding out the next smaller elements in the stack for all elements
for i in range(len(original) - 1, -1, -1):
    while len(stack_2) > 0 and original[stack_2[-1]] >= original[i]:
        stack_2.pop()
        
    if len(stack_2) > 0:
        shorter[i] = stack_2[-1]
    else:
        shorter[i] = -1
        
    stack_2.append(i)
    
solution = []

# This part is just to print out results

for i in range(len(greater)):
    if greater[i] == -1:
        solution.append(str(-1))
    else:
        if shorter[greater[i]] == -1:
            solution.append(str(-1))
        else:
            solution.append(str(original[shorter[greater[i]]]))
            
print(" ".join(solution))

    
    
