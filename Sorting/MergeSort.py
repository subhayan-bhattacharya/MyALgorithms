def mergesort(arr):
    start = 0
    end = len(arr) - 1
    length = len(arr)
    if length < 2:
        return arr
    else:
        pivot = int(len(arr)/2)
        left = mergesort(arr[:pivot])
        right = mergesort(arr[pivot:])
        return merge(left,right)
        
        
def merge(left,right):
    final = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                final.append(left[0])
                del left[0]
            elif right[0] < left[0]:
                final.append(right[0])
                del right[0]
            else:
                final.append(left[0])
                final.append(right[0])
                del right[0]
                del left[0]
        elif len(left) > 0:
            final.extend(left)
            left = []
        else:
            final.extend(right)
            right = []
    
    return final
    

    
      

arr = list(map(int,input().split(" ")))
print ("The input array is:",arr)

final = mergesort(arr)
print ("The final sorted array is:",final)
