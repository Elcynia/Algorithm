import sys
# sys.stdin = open('./input.txt', 'rt')
M, N= map(int, sys.stdin.readline().split())

primes = []
def eratosthenes(n):
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes

primes = eratosthenes(N)

for prime in primes:
    if prime >= M:
        print(prime)