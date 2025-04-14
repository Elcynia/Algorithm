import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
  year = int(input())
  print('Good' if not (year + 1) % ( year%100 ) else 'Bye')
