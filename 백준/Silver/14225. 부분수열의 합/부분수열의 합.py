import sys
input = sys.stdin.readline
N = int(input())
S = list(map(int, input().strip().split(' ')))
result = 0
S.sort()

for i in S:
  if result + 1 < i:
    break
  result += i

print(result + 1)

