import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
T = int(input())
unit = [25, 10, 5, 1]
for i in range(T):
  n = int(input())
  for j in unit:
    print(n//j, end=' ')
    n = n % j
  print()