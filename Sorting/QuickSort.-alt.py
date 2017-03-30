# Python Implementation of quicksort algorithm #
#This is not a good implementation since we are making too many temporary arrays #


def quicksort(arr):
    same = []
    more = []
    less = []
    if len(arr) > 1:
        start = 0
        end = len(arr) - 1
        pivot = arr[int(start + (end - start)/2)]
        
        for i in range(0,len(arr)):
            if arr[i] == pivot:
                same.append(arr[i])
            elif arr[i] > pivot:
                more.append(arr[i])
            elif arr[i] < pivot:
                less.append(arr[i])
        
        final = quicksort(less) + same + quicksort(more)
        
        return final
    else:
        return arr
        



arr = list(map(int,input().split(" ")))
#print ("The input array is:",arr)

final = quicksort(arr)
    
print ("The final sorted array:",final)