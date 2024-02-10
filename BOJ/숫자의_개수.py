import sys
sys.stdin = open('./input.txt', 'rt')

if __name__ == "__main__":
  a = int(input())
  b = int(input())
  c = int(input())
  res = a*b*c
  cnt = [0]*10 # 0~9 까지 숫자 칸 생성
  for i in str(res):
      cnt[int(i)] += 1

  for i in cnt:
      print(i)