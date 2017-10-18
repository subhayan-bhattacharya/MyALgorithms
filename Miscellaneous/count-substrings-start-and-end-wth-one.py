# http://www.geeksforgeeks.org/given-binary-string-count-number-substrings-start-end-1/
str1 = "00100101"
count = 0
for i in str1:
    if i == "1":
        count = count + 1
final = count * (count - 1)//2
print (final)