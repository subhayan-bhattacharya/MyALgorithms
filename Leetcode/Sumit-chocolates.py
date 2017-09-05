n = int(input())
l1 = list(map(int,input().split(' ')))
l2 = []
for index,key in enumerate(l1):
    if index == 0:
        l2.append(key)
    else:
        val = l2[-1] + key
        l2.append(val)
    
def bin_search(arr,start,end,pos):
    if start <= end:
        mid = int(start + (end - start)/2)
        if arr[mid] == pos:
            return mid
        elif arr[mid] > pos:
            if arr[mid - 1] < pos:
                return mid
            elif arr[mid - 1] == pos:
                return mid -1
            else:
                return bin_search(arr,start,mid - 1,pos)
        else:
            return bin_search(arr,mid+1,end,pos)
    else:
        if start > end:
            return start
        else:
            return end
            
q = int(input())
for i in range(q):
    pos = int(input())
    final_pos = bin_search(l2,0,len(l2) - 1,pos)
    print (final_pos + 1)