# Python implementation of Bubblesort algorithm #
def Bubblesort(l):
    last = len(l) - 1
    for i in range(0,last):
        for j in range(0,last):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    



arr = list(map(int,input().split(" ")))
print ("Array before sorting is:",arr)

Bubblesort(arr)
print ("Array after sorting is:",arr)
        
    