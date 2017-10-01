from functools import reduce

def find_gcd(a,b):

    while a != b:
        if a > b:
            a = a -b 
        else:
            b = b - a
    return a
    
def find_lcm(a,b):
    multiply = a * b
    gcd = find_gcd(a,b)
    return multiply // gcd
    
    
r1 = range(1,21)
value = reduce(lambda x,y:find_lcm(x,y),r1)
print (value)