#https://www.geeksforgeeks.org/next-greater-element/
# This is an easier implementation using stacks the logic of which can be found in hackerearth solved problems

def printNGE(arr):
    greater = [-1] * len(arr)
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        while len(stack) > 0 and stack[-1] <= arr[i]:
            stack.pop()
            
        if len(stack) != 0:
            greater[i] = stack[-1]
        else:
            greater[i] = -1
            
        stack.append(arr[i])
    
    return greater
        

arr = [5, 1, 9, 2, 5, 1, 7]
print(printNGE(arr))