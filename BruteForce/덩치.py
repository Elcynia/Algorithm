import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
  weight, height = map(int, input().split())
  arr.append([weight,height])
  
for i in range(n):
  rank = 1
  for j in range(n):
    if (arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]):
      rank += 1
  print (rank, end=' ')