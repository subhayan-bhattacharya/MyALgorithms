# https://leetcode.com/problems/count-primes/description/
# https://www.geeksforgeeks.org/sieve-of-eratosthenes/

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        count = 0
        primes = [True for i in range(n+1)]
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * 2,n+1,p):
                    primes[i] = False
            p = p + 1
        for i in range(2,n):
            if primes[i]:
                count = count + 1

        return count