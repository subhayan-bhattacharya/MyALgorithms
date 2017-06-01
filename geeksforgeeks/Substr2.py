def getsubstrings(str):
    sub = []
    length = len(str)
    for i in range(length):
        for j in range(i,length):
            if str[i] == str[j]:
                sub.append(str[i:j+1])
    return sub
    
str = "abcabba"
final = getsubstrings(str)
print (final)
print (len(final))