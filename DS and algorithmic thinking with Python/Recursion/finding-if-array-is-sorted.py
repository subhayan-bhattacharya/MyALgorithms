# Find if an array is sorted using recursion. 

def find_array_is_sorted(arr):
    if len(arr) == 1:
        return True
    else:
        if arr[0] <= arr[1] and find_array_is_sorted(arr[1:]):
            return True
            
    return False
    
arr = [1,4,2,9,7]
if find_array_is_sorted(arr):
    print("Sorted")
else:
    print("Not sorted")
        