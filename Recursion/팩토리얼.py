import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

n = int(input())
def Factorial(n):
    if (n == 0): return 1
    return n * Factorial(n-1)

print (Factorial(n))