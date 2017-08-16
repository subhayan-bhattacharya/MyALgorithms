# Find the excel column number from column name
import collections

columnname = input()
alphabets = "abcdefghijklmnopqrstuvwxyz"

alphabets_dict = collections.OrderedDict()
for index,key in enumerate(alphabets):
    alphabets_dict[key.upper()] = index + 1
    
value = 0
multiply = 1

for letter in columnname[::-1]: 
    letter = letter.upper()
    value = value + alphabets_dict[letter] * multiply
    multiply = multiply * 26
    
print (value)
    