import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
arr = sum([(K + 1) // 2 for K in list(map(int, input().split()))])

if (arr >= N):
  print ("YES")
else:
  print ("NO")