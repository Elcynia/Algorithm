import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
s = list(input().strip())
cnt = 0

for i in range(len(s)):
  if s[i] == 'Y':
    cnt += 1
    for j in range(i, len(s), i+1):
      s[j] = 'N' if s[j] == 'Y' else 'Y'

print (cnt)