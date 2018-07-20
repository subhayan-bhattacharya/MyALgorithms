import time
import random

def calculatePrimeFactors(n):
    primefaq = []
    d = 2
    while d*d <= n:
        while n % d == 0:
            primefaq.append(d)
            n = n // d
        d = d + 1
    if n > 1:
        primefaq.append(n)
    return primefaq

def main():
    t0 = time.time()
    for i in range(10000):
        rand = random.randint(20000, 100000000)
        print(calculatePrimeFactors(rand))
    t1 = time.time()
    totalTime = t1 - t0

    print(f"Total execution time : {totalTime}")

if __name__ == "__main__":
    main()

