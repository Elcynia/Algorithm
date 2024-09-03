import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
T = int(input())

for i in range(T):
  a = str(input().strip())
  b = str(input().strip())
  cnt = 0
  for j in range(len(a)):
    if a[j] != b[j]:
      cnt += 1
  print(f"Hamming distance is {cnt}.")