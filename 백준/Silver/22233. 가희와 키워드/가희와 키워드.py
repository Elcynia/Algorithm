import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split()) # 메모장, 블로그
keywords = {input().strip() for _ in range(N)}

blogs = [input().strip().split(',') for _ in range(M)]
for blog in blogs:
  for word in blog:
    if word in keywords:
      keywords.remove(word)
    
  print(len(keywords))