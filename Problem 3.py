# Project Euler Problem 3
# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the largest prime factor of the number 600851475143?

import math

def largestPrimeFactor(n):
    res = 2
    
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if isPrime(i):
            if n % i == 0:
                res = i
    return res
    
def isPrime(x):
    for j in range(2, math.floor(math.sqrt(x)) + 1):
        if x % j == 0:
            return False
    return True

print(largestPrimeFactor(600851475143))