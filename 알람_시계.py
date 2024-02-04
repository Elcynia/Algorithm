import sys
sys.stdin = open('./input.txt', 'rt')

if __name__ == "__main__":
  h, m = map(int, input().split())
  if m >= 45:
      m -= 45
  else:
      m += 15
      h = (h - 1 + 24) % 24 # 24시간 형식, 음수제거
  print(h, m)