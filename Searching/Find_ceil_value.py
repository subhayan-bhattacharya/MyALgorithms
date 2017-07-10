arr = tuple(map(int,input().split(' ')))
key = int(input())
ceil = -1

def find_ceil(arr,key,low,high):
    global ceil
    if low <= high:
        mid = int((low + high) / 2)
        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] > key:
            ceil = arr[mid]
            return find_ceil(arr,key,low,mid - 1)
        else:
            return find_ceil(arr,key,mid + 1,high)
    return ceil

check = find_ceil(arr,key,0,len(arr) - 1)
if check == -1:
    print ("Ceil does not exist in the array")
else:
    print (check)