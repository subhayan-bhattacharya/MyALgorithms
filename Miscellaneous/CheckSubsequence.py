# Check if str1 is a subsequence of str2
# http://www.geeksforgeeks.org/given-two-strings-find-first-string-subsequence-second/

def checksubsequence(str1,str2,m,n):
    if m == 0:
        return True
    if n == 0:
        return False
    if str1[m]  == str2[n]:
        return checksubsequence(str1,str2,m-1,n-1)
    return checksubsequence(str1,str2,m,n-1)
   
str1 = input()
str2 = input()
m = len(str1) - 1
n = len(str2) - 1
if checksubsequence(str1,str2,m,n):
    print ("It is a subsequence")
else:
    print ("It is not a subsequence")