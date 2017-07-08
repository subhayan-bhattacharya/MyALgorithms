# An element in a sorted array can be found in O(log n) time via binary search. 
# But suppose we rotate an ascending order sorted array at some pivot unknown to you beforehand. 
# So for instance, 1 2 3 4 5 might become 3 4 5 1 2. Devise a way to find an element in the rotated array in O(log n) time.
# The idea is to find the pivot point, divide the array in two sub-arrays and call binary search.
# The main idea for finding pivot is – for a sorted (in increasing order) and pivoted array, 
# pivot element is the only only element for which next element to it is smaller than it.


def find_pivot(arr):
    for index,ele in enumerate(arr):
        if ele > arr[index + 1]:
            print ("Pivot is :",index+1)
            return (index+1)
            
def binary_search(arr,start,end,element):
    if start <= end:
        mid = int(start + (end - start)/2)
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            return binary_search(arr,mid + 1,end,element)
        else:
            return binary_search(arr,0,mid - 1,element)
    else:
        return None
        

arr = list(map(int,input().split(' ')))
element = int(input())
pivot = find_pivot(arr)
pos = binary_search(arr,0,pivot - 1,element)
if pos is None:
    pos = binary_search(arr,pivot,len(arr) - 1,element)
    if pos is None:
        print ("Element is not there")
    else:
        print (pos)
else:
    print (pos)
    

    
            

        
        


                          



