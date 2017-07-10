arr = tuple(map(int,input().split(' ')))
key = int(input())
floor = -1

def find_floor(arr,key,low,high):
    global floor
    if low <= high:
        mid = int((low + high) / 2)
        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] > key:
            return find_floor(arr,key,low,mid - 1)
        else:
            floor = arr[mid]
            return find_floor(arr,key,mid + 1,high)
    return floor

check = find_floor(arr,key,0,len(arr) - 1)
if check == -1:
    print ("Floor does not exist in the array")
else:
    print (check)
    