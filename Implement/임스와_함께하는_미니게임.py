import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, K = input().split()
players = set()
types = {'Y': 1, 'F': 2, 'O': 3}
for _ in range(int(N)):
  players.add(input().strip())
  
cnt = len(players)
r = cnt // types[K]

print(r)