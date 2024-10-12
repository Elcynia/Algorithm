import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
s = input().strip()
r = set()
for i in range(len(s)):
  for j in range(i + 1, len(s) + 1):
    r.add(s[i:j])
print (len(r))