import time
import random
from multiprocessing import Process

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

def executeProc():
    for i in range(1000):
        rand = random.randint(20000, 100000000)
        print(calculatePrimeFactors(rand))

def main():
    t0 = time.time()
    procs = []
    for i in range(10):
        proc = Process(target=executeProc, args=())
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()
    t1 = time.time()
    totalTime = t1 - t0

    print(f"Total execution time : {totalTime}")

if __name__ == "__main__":
    main()