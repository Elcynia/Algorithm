import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
dist = [list(map(int, input().strip().split())) for _ in range(9)]
r = 0
row, col  = 0, 0
for i in range(9):
  for j in range(9):
    if r <= dist[i][j]:
      r = dist[i][j]
      row = i+1
      col = j+1

print (r)
print (row, col)