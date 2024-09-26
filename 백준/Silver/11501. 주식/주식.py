import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  N = int(input())
  stocks = list(map(int, input().split()))
  mx_price = 0
  amount = 0
  for i in range(N-1, -1, -1):
    if stocks[i] > mx_price:
      mx_price = stocks[i]
    else:
      amount += mx_price - stocks[i]
  print (amount)