import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N = int(input())
arr = input().strip()
red_count = arr.count('R')
blue_count = N - red_count

# 공이 전부 같은 색일 때는 이동 X
if red_count == 0 or blue_count == 0:
    print(0)
else:
  red_left = 0
  blue_left = 0
  for ball in arr:
      if ball == 'R':
          red_left += 1
      else:
          break
  for ball in arr:
      if ball == 'B':
          blue_left += 1
      else:
          break
  # 오른쪽에서 연속된 빨간 공과 파란 공을 각각 카운트
  red_right = 0
  blue_right = 0
  for ball in reversed(arr):
      if ball == 'R':
          red_right += 1
      else:
          break
  for ball in reversed(arr):
      if ball == 'B':
          blue_right += 1
      else:
          break
  red_move = min(red_count - red_left, red_count - red_right)
  blue_move = min(blue_count - blue_left, blue_count - blue_right)
  print(min(red_move, blue_move))