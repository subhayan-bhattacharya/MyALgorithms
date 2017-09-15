def find_ceil(arr,start,end,element):
    if arr[start] > element:
        return start
    if arr[end] < element:
        return -1
    
    mid = int(start + (end - start)/2)
    if arr[mid] == element:
        return mid
    elif arr[mid] > element:
        if arr[mid-1] < element:
            return mid
        elif arr[mid -1] == element:
            return mid -1
        else:
            return find_ceil(arr,start,mid - 1)
    else:
        if arr[mid + 1] >= element:
            return mid +1
        else:
            return find_ceil(arr,mid+1,end)
 


l = [1,2,4,6,11]
element = 5
position = find_ceil(l,0,len(l) - 1,element)
print ("The position of the ceil element is:",position)