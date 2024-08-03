import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = sorted(input().strip(), reverse=True)
ans = 0

if not '0' in n:
    print(-1)
    
else:
  for i in n:
    ans += int(i)
  if ans % 3 != 0:
    print(-1)
  else:
    print (*n, sep='')