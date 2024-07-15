import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
score = 0
for i in range(5):
  n = int(input())
  if (n < 40):
    n = 40
  score += n
print (score // 5)