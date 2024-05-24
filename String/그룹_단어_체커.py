import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
cnt = 0

for i in range(n):
  word = list(input().strip())
  for i in range(1, len(word)):
    if word[i] != word[i - 1] and word[i] in word[:i - 1]:
      break
  else:
      cnt += 1
print (cnt)