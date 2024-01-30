import sys
sys.stdin = open('./input.txt', 'rt')
n = int(input())
answer = []
for i in range(n):
  answer.append(int(input()))
answer.sort()
for i in answer:
  print (i)