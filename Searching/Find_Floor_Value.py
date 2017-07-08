# Given an array of N distinct integers, find floor value of input ‘key’. Say, A = {-1, 2, 3, 5, 6, 8, 9, 10} and key = 7, we should return 6 as outcome.

# We can use the above optimized implementation to find floor value of key. We keep moving the left pointer to right most as long as the invariant holds. 
# Eventually left pointer points an element less than or equal to key (by definition floor value).



def find_floor(arr,start,end,key):
    if start < end:
        mid = int(start + (end - start)/2)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return find_floor(arr,mid + 1,end,key)
        elif arr[mid] > key:
            return find_floor(arr,start,mid - 1,key)
    else:
        if arr[start] <= key:
            return start
        else:
            return -1
            
            

arr1 = list(map(int,input().split(' ')))
key = int(input())
check = find_floor(arr1,0,len(arr1) - 1,key)
if check == -1:
    print ("No possible floor value")
else:
    print ("Floor value is:",arr1[check])


