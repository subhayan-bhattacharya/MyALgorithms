n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
x = [int(x_temp) for x_temp in input().strip().split(' ')]
sorted_x = sorted(x)
print(sorted_x)
i = 0
counter = 0
while i < n:
    counter += 1
    loc = sorted_x[i] + k
    while i < n and sorted_x[i] <= loc:
        i += 1
    i = i - 1
    loc = sorted_x[i] + k
    while i < n and sorted_x[i] <= loc:
        i += 1
print (counter)