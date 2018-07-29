primes = []
count = 1
start = 2
def check_is_prime(n):
    if n <= 3:
        return True
    else:
        for i in primes:
            if n % i == 0:
                return False
        return True
    
while True:
    if check_is_prime(start):
        if count == 10001:
            print (start)
            break
        else:
            primes.append(start)
            count = count + 1
    start = start + 1
print(primes)
          
        