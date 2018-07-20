def genfibonacci(num):
    f = [0] * (num + 1)
    f[1] = 1
    for i in range(2,num+1):
        f[i] = f[i-2] + f[i-1]
    print (f'Fibonacci series : {f}')

for i in range(10,15):
    genfibonacci(i)