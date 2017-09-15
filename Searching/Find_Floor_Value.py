def find_floor(arr,start,end,element):
    if arr[start] > element:
        return -1
    if arr[end] <= element:
        return end
    
    mid = int(start + (end - start)/2)
    if arr[mid] == element:
        return mid
    elif arr[mid] < element:
        if arr[mid+1] == element:
            return mid +1
        elif arr[mid+1] > element:
            return mid
        else:
            return find_floor(arr,mid+1,end,element)
    else:
        if arr[mid -1] < element:
            return mid - 1
        elif arr[mid -1] == element:
            return mid - 1
        else:
            return find_floor(arr,start,mid -1,element)
            


arr = [1,2,8,10,10,12,19]
element = 5
position = find_floor(arr,0,len(arr) - 1,element)
print ("The position of the floor element is:",position)