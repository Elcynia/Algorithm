import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, K = map(int, input().strip().split())
    
    while N and K:
        N //= 2
        K -= 1
    print((N + 1) // 2)