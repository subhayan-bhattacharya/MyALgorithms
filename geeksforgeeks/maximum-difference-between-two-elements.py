# https://www.geeksforgeeks.org/maximum-difference-between-two-elements/

arr = [10,9,8,7,6]
min_value = arr[0]
max_diff = 0
for index,key in enumerate(arr):
    if index == 0:
        continue
    else:
        if key <= min_value:
            min_value = key
        else:
            diff = key - min_value
            if diff > max_diff:
                max_diff = diff
print (max_diff)