# Given two unsorted arrays arr1[] and arr2[]. They may contain duplicates. 
# For each element in arr1[] count elements less than or equal to it in array arr2[].
#http://www.geeksforgeeks.org/element-1st-array-count-elements-less-equal-2nd-array/

def find_less_than_equalto(arr,start,end,key):
    if start <= end:
        mid = int(start + (end - start)/2)
        if arr[mid] == key:
            return find_less_than_equalto(arr,mid+1,end,key)
        elif arr[mid] < key:
            return find_less_than_equalto(arr,mid+1,end,key)
        else:
            return find_less_than_equalto(arr,start,end - 1,key)
    else:
        return end

arr1 = [1, 2, 3, 4, 7, 9]
arr2 = [0,1,2,1,1,4]
sorted_arr2 = sorted(arr2)
print (sorted_arr2)
for m in arr1:
    check = find_less_than_equalto(sorted_arr2,0,len(sorted_arr2) - 1,m)
    print ("Elements less than or equal to: ",m," is: ",(check + 1))


