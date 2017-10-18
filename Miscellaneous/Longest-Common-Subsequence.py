# Logic for the code : https://www.youtube.com/watch?v=NnD96abizww

s1 = "AGGTAB"
s2 = "GXTXAYB"
m = len(s1)
n = len(s2)
l = [[0] * (m+1) for i in range(n+1)]
track = [[0] * (m+1) for i in range(n+1)]
#print (l)

for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[j - 1] != s2[i - 1]:
            l[i][j] = max(l[i-1][j],l[i][j-1])
            if l[i-1][j] > l[i][j - 1]:
                track[i][j]  = 'u'
            else:
                track[i][j] = 'l'
        else:
            l[i][j] = l[i-1][j-1] + 1
            track[i][j] = 'd'
          
print (l[n][m])

# for i in range(len(l)):
    # print (l[i])
    
# print ("==================")

# for i in range(len(track)):
    # print (track[i])

i = n
j = m
subsequence = []

while track[i][j] != 0:
    if track[i][j] == 'd':
        print ("Adding:",s1[j-1])
        subsequence.append(s1[j - 1])
        i = i - 1
        j = j - 1
    elif track[i][j] == 'u':
        i = i - 1
    else:
        j = j - 1
        
print (subsequence[::-1])

        