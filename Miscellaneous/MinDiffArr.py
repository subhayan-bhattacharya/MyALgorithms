#Find the minimum absolute difference between any two elements of an array#

num = int(input())
l = list(map(int,input().split(' ')))
min = []
sorted_l = sorted(l)
length = len(sorted_l)
for i in range(length-1):
    diff = abs(sorted_l[i] - sorted_l[i+1])
    min.append(diff)
 
sorted_min = sorted(min) 
print (sorted_min[0])