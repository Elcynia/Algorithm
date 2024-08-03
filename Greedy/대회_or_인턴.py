import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n, m, k = map(int,input().split()) # 남1, 녀2, 인턴십 k

teams = min(n // 2, m)

while (n + m - 3 * teams) < k:
  teams -= 1

print(teams)