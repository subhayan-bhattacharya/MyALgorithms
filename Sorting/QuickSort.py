# Python Implementation of quicksort algorithm #
#This is a better implementation since we are not using any temporary arrays and we are relying on swapping #

def partition(arr,left,right):
    pivot = arr[right]
    i = left
    for j in range(left,right):
        if arr[j] <= pivot:
            arr[j],arr[i] = arr[i],arr[j]
            print ("Swapping:",j,"and:",i)
            i = i + 1
    arr[i],arr[right] = arr[right],arr[i]
    print ("Finally swapping:",i,"and:",right)
    print ("Sorted array at the end of the partition step is:",arr)
    return i
    
def quicksort(arr,start,end):
    if start < end:
        pivot = partition(arr,start,end)
        print ("Pivot position is:",pivot)
        quicksort(arr,start,pivot - 1)
        quicksort(arr,pivot + 1,end)
   
          
           

arr = list(map(int,input().split(" ")))
quicksort(arr,0,len(arr) - 1)
    
print ("The final sorted array:",arr)