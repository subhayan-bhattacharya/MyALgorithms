#http://www.geeksforgeeks.org/minimum-sum-two-elements-two-arrays-indexes-not/

# Given two arrays a[] and b[] of same size. 
# Task is to find minimum sum of two elements such that they belong to different arrays and are not at same index in their arrays.

arr1 = [5, 4, 13, 1]
arr2 = [3, 2, 6, 1]

d1 = {x:index for index,x in enumerate(arr1)}
d2 = {y:index for index,y in enumerate(arr2)}

sorted_arr1 = sorted(arr1)
sorted_arr2 = sorted(arr2)

#print (d1[sorted_arr1[0]],d2[sorted_arr2[0]])

if d1[sorted_arr1[0]] != d2[sorted_arr2[0]]:
    print (sorted_arr1[0] + sorted_arr2[0])
else:
    print (min((sorted_arr1[0] + sorted_arr2[1]),(sorted_arr1[1] + sorted_arr2[0])))

    