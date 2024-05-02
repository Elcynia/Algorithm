import sys
# sys.stdin = open('./input.txt', 'rt')

if __name__ == "__main__":
  n = list(map(int, input().split(' ')))
  answer = 0
  for i in n:
    answer += i*i
  print (answer%10)