# import sys
# sys.stdin = open('./input.txt', 'rt')
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

if __name__ == "__main__":
  n = int(input())
  if (n % 4 == 0 and (n % 100!=0 or n%400 == 0)):
    print (1)
  else:
    print (0)
  