number = 100
divisors = set()
limit = number // 2
for i in range(1,limit+1):
    if number % i == 0:
        quotient = number // i
        divisors.add(i)
        divisors.add(quotient)
        
print (divisors)