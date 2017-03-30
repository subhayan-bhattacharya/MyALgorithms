# Python Implementation of insertion sort #
# The important theme to remember is that the left part of the array would always be automatically sorted #
#So for every element we go on checking the elements before it and whenever i find that the element compared is less than that element
#swap positions #

# Worst case running time of insertion sort is n square as per big o #

def insertionsort(arr,start,end):
    if start <= end:
        if start != 0:
            insertmin(arr,start,end)
        insertionsort(arr,start + 1,end)
    else:
        return
        
        
def insertmin(arr,start,end):
    index = start
    for i in range(start - 1, -1, -1):
        if arr[index] < arr[i]:
            arr[index],arr[i] = arr[i],arr[index]
            index = i
    

arr = list(map(int,input().split(" ")))
print ("Array before sorting is:",arr)

insertionsort(arr,0,len(arr) - 1)
print ("Array after sorting is:",arr)