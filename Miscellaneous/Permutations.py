#Used to find permutations of a given string
#Logic from the youtube video : https://www.youtube.com/watch?v=iFafKAUGqrY&t=244s

def permutation(lst,i,n):
    if i == n:
        print (lst)
    else:
        for j in range(i,n+1):
            lst[i],lst[j] = lst[j],lst[i]
            permutation(lst,i+1,n)
            lst[i],lst[j] = lst[j],lst[i]

        
data = list('MAN')
permutation(data,0,len(data) - 1)
            