import operator
loop = int(input())
count = {}
scores = {}
for i in range(loop):
    id,score = list(map(int,input().split(' ')))
    if id in scores:
        scores[id] += score
        count[id] += 1
    else:
        scores[id] = score
        count[id] = 1
for id in scores:
    scores[id] = scores[id] / count[id]
sorted_scores = sorted(sorted(scores.items(),key=operator.itemgetter(0)), key=operator.itemgetter(1),reverse=True)
print (sorted_scores)


    
    
        

