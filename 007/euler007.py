from itertools import count, islice
from math import sqrt

def isPrime(num):
    return all(num%i for i in islice(count(2), int(sqrt(num))-1))

def init_primes():

    primes = [2]

    N = 10**4
    i = 3

    while len(primes) <= N:

        if isPrime(i):
            primes.append(i)

        i += 1

    return primes


precomputed_primes = init_primes()

tests = int(raw_input())

for test in xrange(tests):

    N = int(raw_input())

    print precomputed_primes[N-1]
    