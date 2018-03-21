#https://www.geeksforgeeks.org/count-pairs-two-sorted-matrices-given-sum/
# This used binary search  approach


import sys

def less_than_or_equal_to(arr,num,start,end):
    mid = int(start + (end - start)/2)
    #print "Mid index is {}".format(mid)
    if arr[end] <= num:
        return end
    if arr[mid] == num:
        return mid
    elif arr[mid] < num and arr[mid + 1] > num:
        return mid
    elif arr[mid] > num and arr[mid - 1] <= num:
        return mid - 1
    elif arr[mid] > num:
        return less_than_or_equal_to(arr,num,start,mid - 1)
    elif arr[mid] < num:
        return less_than_or_equal_to(arr,num,mid + 1,end)
	
	
def binary_search(arr,num,start,end):
	if start <= end:
		mid = int(start + (end - start)/2)
		if arr[mid] < num:
			return binary_search(arr,num,mid + 1,end)
		elif arr[mid] > num:
			return binary_search(arr,num,start,mid - 1)
		else:
			return arr[mid]
	else:
		return None
		
arr1 = [map(int,raw_input().split(",")) for i in range(3)]
print (arr1)
arr2 = [map(int,raw_input().split(",")) for i in range(3)]
print (arr2)

first_col_arr2 = [arr[0] for arr in arr2]

#print first_col_arr2

#sys.exit(0)

key = int(raw_input())
pairs = []
end = False

for arr in arr1:
    #print arr
    for a in arr:
        #print "Starting for a :{}".format(a)
        if a > key:
            #print pairs
            #print "a {} is more than key {}".format(a,key)
            end = True
            break
        else:
            diff = key - a
            #print "Diff {} for a {}".format(diff,a)
            if diff < first_col_arr2[0]:
                #print "Difference {} is more than the first element in second array {}".format(diff,first_col_arr2[0])
                print pairs
                end = True
                break
            index = less_than_or_equal_to(first_col_arr2,diff,0,len(first_col_arr2) - 1)
            #print "The index of the row is : {}".format(index)
            if first_col_arr2[index] == diff:
                t = (a,first_col_arr2[index])
                pairs.append(t)
                #print "After appending value of pairs is : ",pairs
                #break
            else:
                element = binary_search(arr2[index],diff,0,len(arr2[index]) - 1)
                if element is not None:
                    t = (a,element)
                    pairs.append(t)
                    #print "After appending value of pairs is : ",pairs
                    #break
        #print "At the end of the whole process a is {}".format(a)
    if end:
        break
print (pairs)
			

