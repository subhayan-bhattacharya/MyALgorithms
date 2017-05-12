#Hackerrank problem : Organizing container of balls #

q = int(input())
for j in range(q):
    n = int(input())
    ballcount = [0] * n
    box = []
    for i in range(n):
        balls = list(map(int,input().split(' ')))
        box.append(sum(balls))
        for index,ball in enumerate(balls):
            ballcount[index] = ballcount[index] + ball
    sorted_box = sorted(box)
    sorted_ballcount = sorted(ballcount)
    print (sorted_box)
    print (sorted_ballcount)
    if sorted_box == sorted_ballcount:
        print ("Possible")
    else:
        print ("Impossible")
