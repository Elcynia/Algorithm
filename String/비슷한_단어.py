import sys
from collections import Counter
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
cnt = 0
first_word = input().rstrip()
first_counter = Counter(first_word)
for i in range(n-1):
  word = input().rstrip()
  word_counter = Counter(word)
  if abs(len(first_word) - len(word)) > 1:
    continue
  diff = sum((first_counter - word_counter).values()) + sum((word_counter - first_counter).values())
  if (diff <= 2): # 차이가 2이상이 아니면 비슷한 단어로 간주
    cnt += 1
print (cnt)