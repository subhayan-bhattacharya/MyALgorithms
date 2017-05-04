def merge_intervals(intervals):
    sorted_by_lower_bound = sorted(intervals, key=lambda tup: tup[0])
    merged = []
    for higher in sorted_by_lower_bound:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            if higher[0] < lower[1]:
                upper_bound = max(lower[1],higher[1])
                merged[-1] = (lower[0],upper_bound)
            else:
                merged.append(higher)
    return merged

    
#intervals = [(0,1),(2,4),(6,7),(3,5)]
intervals = []
count = int(input())
for i in range(count):
    t = tuple(map(int,input().split(' ')))
    intervals.append(t)
check = merge_intervals(intervals)
print (check)

    



    
    
            
            
        


        