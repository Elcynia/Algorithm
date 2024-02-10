import sys
sys.stdin = open('./input.txt', 'rt')
if __name__ == "__main__":
  n = int(input())
  
  for _ in range(n):
    cnt = 0
    score = 0
    arr = str(input())
    for i in arr:
      if (i == 'O'):
        cnt += 1
        score += cnt
      else:
        cnt = 0
    print (score)
