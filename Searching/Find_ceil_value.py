#http://www.geeksforgeeks.org/ceiling-in-a-sorted-array/

def find_ceil(arr,start,end,key):
    if start < end:
        mid = int(start + (end - start)/2)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return find_ceil(arr,mid+1,end,key)
        else:
            return find_ceil(arr,start,mid - 1,key)
    else:
        if arr[start] >= key:
            return start
        else:
            return -1
            
arr1 = list(map(int,input().split(' ')))
key = int(input())
index = find_ceil(arr1,0,len(arr1) - 1,key)
if index == -1:
    print ("The ceiling does not exist in the array")
else:
    print ("The ceiling element is: ",arr1[index])