import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
cnt = 0
r = set()
for i in range(n):
  chat = input().strip()
  if chat == 'ENTER':
    cnt += len(r)
    r.clear()
  else:
    r.add(chat)
cnt += len(r)
print (cnt)