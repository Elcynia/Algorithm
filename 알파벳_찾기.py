import sys
# sys.stdin = open('./input.txt', 'rt')
if __name__ == "__main__":
  n = str(input())
  ans = []
  alpha = list(range(97,123))
  for i in alpha:
     print (n.find(chr(i)), end=' ')
