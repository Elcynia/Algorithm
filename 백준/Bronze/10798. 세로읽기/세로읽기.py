import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
board = [input().strip() for _ in range(5)]

for i in range(15):
  for j in range(5):
    if i < len(board[j]):
      print (board[j][i], end='')