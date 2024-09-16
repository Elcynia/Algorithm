import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N = input().strip()
idx = 0
num = 1

while idx < len(N):
  current = str(num)
  for digit in current:
    if idx < len(N) and digit == N[idx]:
      idx += 1  # N의 다음 문자로 이동
    if idx == len(N):
      break

  num += 1  # 다음 숫자로 이동

print(num - 1)