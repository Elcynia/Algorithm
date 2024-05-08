import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n, k = map(int, input().split())

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)

# nCk = n // k! * (n-k)
print(factorial(n) // (factorial(k) * factorial(n - k)))

