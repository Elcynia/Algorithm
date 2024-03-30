import sys
sys.stdin = open('./input.txt', 'r')
n = int(sys.stdin.readline())
cnt = 0
while(n>0):
  cnt+=n//5
  n//=5
print(cnt)