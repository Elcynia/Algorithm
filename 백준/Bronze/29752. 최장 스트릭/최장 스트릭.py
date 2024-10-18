import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
streak = []
arr = list(map(int, input().strip().split()))
cnt = 0
for i in arr:
  if i > 0:
    cnt += 1
  else:
    streak.append(cnt)
    cnt = 0
  streak.append(cnt)
print (max(streak) if streak else 0)