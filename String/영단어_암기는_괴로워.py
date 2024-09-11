import sys
from collections import Counter
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
words = [input().strip() for _ in range(N)]
filtered_words = [word for word in words if len(word) >= M]
word_count = Counter(filtered_words)
sorted_words = sorted(word_count.keys(), key=lambda x: (-word_count[x], -len(x), x))
print (*sorted_words, sep='\n')