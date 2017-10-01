"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(number):
    str_number = str(number)
    if str_number == str_number[::-1]:
        return True
    else:
        return False

palindromes = []
for i in range(990,99,-1):
    for j in range(999,99,-1):
        value = i * j
        if is_palindrome(value):
            palindromes.append(value)
            
print (sorted(palindromes)[-1])