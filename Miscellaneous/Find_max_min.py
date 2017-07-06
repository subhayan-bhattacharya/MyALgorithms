#Recursive program to find the maximum and minimum element in the array#

arr = [1,2,3,0,34]
def find_max(arr):
    if len(arr) > 1:
        last = arr[-1]
        return max(last,find_max(arr[:-1]))
    else:
        return arr[0]
    
check = find_max(arr)
print (check)