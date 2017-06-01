# How to find all the substrings of a string which start and end with the same letter #
#Related searches
# http://www.geeksforgeeks.org/given-binary-string-count-number-substrings-start-end-1/
# http://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/


def factorial(n):
    if n > 0:
        fact = 1
        for i in range(1,n+1):
            fact = fact * i
        return fact


def getsubstrings(str):
    s = set(str)
    print (s)
    final = 0
    for char in s:
        times = str.count(char)
        print ("Times:",times)
        if times > 1:
            value = factorial(times + 1) // (factorial(2) * factorial(times + 1 - 2))
        else:
            value = 1
        final = final + value
    return final
    
str = "abcabba"
sub = getsubstrings(str)
print (sub)

