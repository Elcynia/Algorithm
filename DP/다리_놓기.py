import sys, math
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
T = int(input())
results = []

def combination(n, m):
    return math.factorial(m) // (math.factorial(n) * math.factorial(m - n))

for _ in range(T):
    N, M = map(int, input().split())
    results.append(combination(N, M))

print (*results, sep='\n')

'''
조합 공식
C(m,n) = m! // n! * (m-n)!
'''
