# From a list of elements find out the element which is not repeated in that list
# all other elements are repeated twice.
#Use binary search

l1 = [1,1,2,3,3,4,4]

def find_single_element(arr,start,end):
    mid = int (start + (end - start) / 2)
    #print ("Mid value: {} at position {}".format(arr[mid],mid))
    if mid == 0 and arr[mid + 1] != arr[mid]:
        return arr[mid]
    elif mid == len(arr) - 1 and arr[mid - 1] != arr[mid]:
        return arr[mid]
    elif arr[mid - 1] != arr[mid] and arr[mid + 1] != arr[mid]:
        return arr[mid]
    elif arr[mid - 1] == arr[mid]:
        remaining = mid - 1
        if remaining % 2 != 0:
            #The lone element is on the left#
            #print ("Should go left for mid value:",arr[mid])
            return find_single_element(arr,start,mid - 2)
        else:
            #The lone element is on the right
            return find_single_element(arr,mid + 1,end)
    elif arr[mid + 1] == arr[mid]:
        remaining = end - mid + 1
        if remaining % 2 != 0:
            #The lone element is on the right#
            #print ("Should go right for mid value:",arr[mid])
            return find_single_element(arr,mid + 2,end)
        else:
            #The lone element is on the left
            return find_single_element(arr,start,mid - 1)

    
start = 0
end = len(l1) - 1
value = find_single_element(l1,start,end)
print (value)