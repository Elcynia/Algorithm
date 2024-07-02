import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
probs = list(map(int, input().split()))
mx = [100, 100, 200, 200, 300, 300, 400, 400, 500]
ans = 0
hacked = 0
for i in range(9):
    if probs[i] > mx[i]:
        hacked = 1
    ans += probs[i]
if hacked:
    print("hacker")
else:
  if ans >= 100:
    print("draw")
  else:
    print("none")