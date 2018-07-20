# https://www.geeksforgeeks.org/making-elements-distinct-sorted-array-minimum-increments/

arr = [3, 4, 6, 8]
sum = arr[0]
prev = arr[0]
for index,key in enumerate(arr):
    if index == 0:
        continue
    else:
        if arr[index] == prev:
            prev = prev + 1
            sum = sum + prev
        else:
            sum = sum + arr[index]
            prev = arr[index]
print (sum