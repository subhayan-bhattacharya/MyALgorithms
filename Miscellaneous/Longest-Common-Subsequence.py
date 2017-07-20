#Not working as per hackerrank

#length1,length2 = tuple(map(int,input().split(' ')))
#str1 = list(map(int,input().split(' ')))
#str2 = list(map(int,input().split(' ')))

str1 = input()
str2 = input()

length1 = len(str1)
length2 = len(str2)


final = []

firstrow = [0] * (length2 + 1)
final.append(firstrow)

for i in range(length1):
    final.append([0])
    
subsequence = []

longest = 0

for index1,val1 in enumerate(str1):
    for index2,val2 in enumerate(str2):
        toadd = 0
        firstindex = index1 + 1
        secondindex = index2 + 1
        if val1 == val2:
            value = final[firstindex - 1][secondindex - 1] + 1
            if value > longest:
                subsequence.append(val1)
                longest = value
        else:
            first = final[firstindex - 1][secondindex]
            second = final[firstindex][secondindex - 1]
            value = max(first,second)
        #print ("trying to add value:",value," to position:",firstindex,secondindex)
        final[firstindex].append(value)
# for rows in final:
    # print (rows)

#print ("The longest common subsequence is:",final[length1][length2])

index = final[length1][length2]
subsequence = [""] * index
i = length1
j = length2

while i > 0 and j > 0:
    if str1[i-1] == str2[j-1]:
        subsequence[index - 1] = str1[i-1]
        i = i - 1
        j = j - 1
        index = index - 1
    else:
        if final[i-1][j] > final[i][j-1]:
            i = i -1
        else:
            j = j -1
subsequencestr = ' '.join(list(map(str,subsequence)))
print (subsequencestr)


            
            