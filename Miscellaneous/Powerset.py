#Python code to generate powersets or subsequences of a string 
#Understand bit wise operators first

def getsubsequences(arr):
    l = len(arr)
    for i in range(1 << l):
        sub = []
        for j in range(l):
            check = i & (1 << j)
            print ("For i:",i," and j:",j," the value of check is:",check)
            if (i & (1 << j)):
                sub.append(arr[j])
        print (sub)
        
getsubsequences([1,2,3])



# from itertools import combinations
# s = [1,2,3]
# pset = set()
# for i in range(len(s) + 1):
    # for sset in combinations(s,i):
        # pset.add(sset)
        
# print (pset)
    