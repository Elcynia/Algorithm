import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
s = input().strip()
arr = [s[i:] for i in range(len(s))]
for i in sorted(arr):
  print (i)
