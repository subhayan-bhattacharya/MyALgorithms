#https://www.geeksforgeeks.org/next-greater-element/

from collections import OrderedDict
def printNGE(arr):
    mappings = OrderedDict()
    stack = []
    element = 0
    next = 0
    stack.append(arr[0])
    mappings[arr[0]] = 0
    for i in range(1,len(arr)):
        mappings[arr[i]] = 0
        next = arr[i]
        element = stack.pop()
        while element < next:
            mappings[element] = next
            if len(stack) != 0:
                element = stack.pop()
            else:
                break
        if element > next:
            stack.append(element)
        stack.append(next)
        
    for s in stack:
        mappings[s] = -1
    for key in mappings:
        print(f'{key}--->{mappings[key]}')
        

arr = [7,1,2,10,5]
printNGE(arr)