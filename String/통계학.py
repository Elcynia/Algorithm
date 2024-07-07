import sys
from collections import Counter
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
cnt = Counter(arr)
print (round(sum(arr)/n))
print (sorted(arr)[n//2])
modes = [k for k, v in cnt.items() if v == max(cnt.values())]
modes.sort()
if (len(modes) > 1):
  print (modes[1])
else:
  print (modes[0])
print (max(arr) - min(arr))