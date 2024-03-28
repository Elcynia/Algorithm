import sys
# sys.stdin = open('./input.txt', 'rt')

N = int(sys.stdin.readline())
coordinates = []
for i in range(N):
  x,y = map(int, input().split()) 
  coordinates.append((x, y))

coordinates.sort(key=lambda coord: (coord[0], coord[1]))
for x,y in coordinates:
  print (x,y)