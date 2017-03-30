# python implementation of selection sort #
# Time complexity is n square in big o notation #

def selectionsort(arr,start,end):
    
    if start < end:
        minindex = findminindex(arr,start)
        
        # Swapping values once the index of the minimum element is found #
        arr[start],arr[minindex] = arr[minindex],arr[start]
        
        #Once the swap is done continue the recursive loop #
        selectionsort(arr,start+1,len(arr) -1)
    
               
def findminindex(arr,start):
    index = start
    # Find the index of the minimum element in the rest of the array #
    for i in range(start+1,len(arr)):
        if arr[index] > arr[i]:
            index = i
    return index
            
   
    
arr = list(map(int,input().split(" ")))
print ("The input array is:",arr)

selectionsort(arr,0,len(arr) - 1)
    
print ("The final sorted array:",arr)
