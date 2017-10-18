import math

def check_if_no_is_prime(n):
    if n <= 3:
        return True
    else:
        limit = int(math.sqrt(n))
        for i in range(2,limit + 1):
            if n % i == 0:
                return False
        return True
        

def find_prime_factors(x):
    prime_factors = []
    if check_if_no_is_prime(x):
        prime_factors.append(1)
        prime_factors.append(x)
    else:
        while x % 2 == 0 and x > 1:
            prime_factors.append(2)
            x = x // 2
        limit = int(math.sqrt(x))
        if limit > x:
            higher_limit = limit
        else:
            higher_limit = x
        for i in range(3,higher_limit+1,2):
            while x % i == 0 and x > 1:
                if check_if_no_is_prime(i):
                    prime_factors.append(i)
                    x = x // i
                if x <= 1:
                    return prime_factors
        return prime_factors
                
no = int(input())
check = find_prime_factors(no)
print (check)
        
    