# Code to check if two strings are anagrams of each other
# http://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/

# NOT RIGHT YET #

def checkanagram(str1,str2):
    l1 = list(str1)
    l2 = list(str2)
    temp = str1
    for c in temp:
        if c in l2:
            l1.remove(c)
            l2.remove(c)
    if len(l1) == 0 and len(l2) == 0:
        return True
    else:
        return False
    
str1 = input()
str2 = input()
if checkanagram(str1,str2):
    print ("It is an anagram")
else:
    print ("Its not an anagrams")
            

