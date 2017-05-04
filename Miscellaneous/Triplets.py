# Erica wrote an increasing sequence of  numbers () in her notebook. She considers a triplet  to be beautiful if:
# i < j < k
# a[j] - a[i] = a[k] - a[j]
# Given the sequence and the value of , can you help Erica count the number of beautiful triplets in the sequence?

def getsustr(numbers,d):
    for i in numbers:
        if (i + d) in numbers and (i + 2 * d) in numbers:
            count = count + 1
    print (count)
        
count,d = tuple(map(int,input().split(' ')))
l1 = list(map(int,input().split(' ')))
check = getsustr(l1,d)