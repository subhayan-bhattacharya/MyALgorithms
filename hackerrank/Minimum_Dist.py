# Hackerrank algorithm problem Minimum Distances #
elements = int(input())
l1 = list(map(int,input().split(' ')))
d1 = {}
min = len(l1)
for index,l in enumerate(l1):
    if l in d1:
        check = abs(d1[l] - index)
        if check < min:
            min = check
        d1[l] = index
    else:
        d1[l] = index

if min == len(l1):
    print (-1)
else:
    print (min)