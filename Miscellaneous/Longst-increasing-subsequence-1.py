#Find out the longest increasing subsequence#
# https://www.youtube.com/watch?v=CE2b_-XfVDk
#http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/

arr = tuple(map(int,input().split(' ')))
l = [1] * len(arr)
i = 1
j = 0
while i <= (len(arr) - 1):
    while j < i:
        if arr[j] < arr[i]:
            l[i] = max(l[j]+1,l[i])
        j = j + 1
        
    i = i + 1
    j = 0
    
print (max(l))
        

