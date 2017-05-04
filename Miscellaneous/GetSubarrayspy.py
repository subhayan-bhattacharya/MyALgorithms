#Get all non empty subarrays of a given list #
#Same method as in getting substrings #

def getsubarrays(arr):
    final = set()
    for i in range(len(arr)+1):
        for j in range(i,len(arr) + 1):
            t = tuple(arr[i:j+1])
            if len(t) > 0:
                final.add(t)
    return final
            
arr = [1,2,3,4]
final = getsubarrays(arr)
for arr in final:
    print (arr)