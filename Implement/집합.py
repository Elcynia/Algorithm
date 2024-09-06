import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
S = set()
def cal(item, num=None):
  global S
  if item == 'add':
    S.add(num)
  elif item == 'remove':
    S.discard(num)
  elif item == 'check':
    print(1 if num in S else 0)
  elif item == 'toggle':
    if num in S:
      S.remove(num)
    else:
      S.add(num)
  elif item == 'all':
    S = set(range(1, 21))
  elif item == 'empty':
    S.clear()
    
for _ in range(n):
  cmd = input().split()
  if len(cmd) == 1:
    cal(cmd[0])
  else:
    cal(cmd[0], int(cmd[1]))
  