import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().strip().split())
a = set()
b = set()

for _ in range(N):
    a.add(input().strip())

for _ in range(M):
    b.add(input().strip())
    
result = sorted(list(a & b))

print(len(result))
for i in result:
    print(i)
    