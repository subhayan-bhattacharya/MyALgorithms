# Tower of hanoi problem. This can be really be confusing so always start with
#getting the algo to work if you just have 2 rings and 3 rods(This does not change)
#So consider rod A(source) , rod(B) as destination and rod(C) as intermediate.
#For 2 rings the output should be : Moving rod 1 from A to C, Moving 2 from A to B, Moving 1 from C to B

def tower_of_hanoi(n, source, mid, dest):
    if n == 1:
        print("Moving ring",n,"from",source,"to",dest)
        return
    tower_of_hanoi(n - 1, source, dest, mid)
    print("Moving ring",n,"from",source,"to",dest)
    tower_of_hanoi(n - 1, mid, source, dest)
    
    
n = int(input())
tower_of_hanoi(n,'A','C','B')
    