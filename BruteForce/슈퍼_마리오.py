import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

ans = 0
arr = [int(input()) for _ in range(10)]

for n in arr:
  ans += n
  if ans >= 100:
    if ans - 100 > 100 - (ans-n):
      ans -= n
    break
print(ans)