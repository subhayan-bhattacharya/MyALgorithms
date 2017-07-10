memo = {}
def fibonacci(n):
    if n in memo:
        return memo[n]
    else:
        if n <= 2:
            f = 1
        else:
            f = fibonacci(n-2) + fibonacci(n-1)
        memo[n] = f
        return f
        
number = int(input())
for i in range(1,number):
    print (fibonacci(i))