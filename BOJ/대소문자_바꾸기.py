import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = list(input())
ans = []
for i in n:
  if (i == i.lower()):
    ans.append(i.upper())
  else:
    ans.append(i.lower())
print(''.join(ans))