import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n, x = map(int, input().split())
socks = list(map(int, input().split()))
ans = []
for i in range(n-1):
  ans.append(socks[i]*x + socks[i+1]*x)
  
print (min(ans))