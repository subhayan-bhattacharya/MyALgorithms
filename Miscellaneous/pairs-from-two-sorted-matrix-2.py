#https://www.geeksforgeeks.org/count-pairs-two-sorted-matrices-given-sum/
#Using best approach


arr1 = [[1,5,6],[8,10,11],[15,16,18]]
arr2 = [[2,4,7],[9,10,12],[13,16,20]]

key = 21

end = len(arr2) - 1
n = 3

row1 = 0
column1 = 0

row2 = n - 1
column2 = n - 1

pairs = []

while row1 < n and row2 > -1:
   
    print "Checking {} and {}".format(arr1[row1][column1],arr2[row2][column2])
    
    value = arr1[row1][column1] + arr2[row2][column2]
    
    if value == key:
        t = (arr1[row1][column1],arr2[row2][column2])
        pairs.append(t)
        column2 = column2 - 1
        column1 = column1 + 1
        
    elif value > key:
        column2 = column2 - 1
    else:
        column1 = column1 + 1
        
    if column1 == n:
        row1 = row1 + 1
        column1 = 0
        
    if column2 == -1:
        row2 = row2 - 1
        column2 = n - 1
        
    print "column1 : {} and column2 : {}".format(column1,column2)
        
print (pairs)
        
    
        
        
        