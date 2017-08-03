#!/usr/bin/python3

# Program to find prime numbers.
# Intended for demonstrating signals
# This version ignores SIGINT

from time import sleep
from signal import *

def isprime(n):
    sleep(0.1)
    x = 2
    while (x * x ) <= n:
        if not n % x:
            return False
        x += 1
    return True

n = 1
primes_list = []
signal(SIGINT, SIG_IGN)

while True:
    if isprime(n):
        print("%d is prime" % n)
        primes_list.append(n)
    n += 1
        
