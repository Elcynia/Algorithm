import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

paper = [[False] * 100 for _ in range(100)]

# 색종이 수 입력
n = int(input())

# 각 색종이에 대해 처리
for _ in range(n):
  r, c = map(int, input().split())
  for i in range(r, r+10):
    for j in range(c, c+10):
      paper[i][j] = True

result = sum(sum(row) for row in paper)

print(result)