def rotate(l,b):
    return l[-b:] + l[:-b]

temp = list(map(int,input().split(' ')))
a = temp[0]
b = temp[1]
l = list(map(int,input().split(' ')))
final = rotate(l,b)
for j in final:
    print (j,end=' ')