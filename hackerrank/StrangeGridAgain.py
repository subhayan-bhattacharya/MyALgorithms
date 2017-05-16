#https://www.hackerrank.com/challenges/strange-grid
#Not fully correct 
#Time out error

def checkstart(row):
    count = 1
    global last 
    while count <= row:
        if count == 1:
            last = 0
            yield last
            count = count + 1
        else:
            if count % 2 == 0:
                last = last + 1
                yield last
                count = count + 1
            else:
                last = last + 2 * 4 + 1
                yield last
                count = count + 1
        

row,column = tuple(map(int,input().split(' ')))
last = 0
check = checkstart(row)
for i in range(row):
    first = next(check)
element = first + 2 * (column - 1)
print (element)
    
