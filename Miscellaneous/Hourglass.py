# Hackerrank problem : https://www.hackerrank.com/challenges/2d-array
arr = [list(map(int,input().split(' '))) for i in range(6)]
#print (arr)
values = []
for i in range(0,4):
    for j in range(0,4):
        hourglass = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        values.append(hourglass)
        sorted_values = sorted(values)
            
print (sorted_values[0])