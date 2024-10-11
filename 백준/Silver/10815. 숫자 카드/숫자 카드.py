import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N = int(input())
cards = set(list(map(int, input().strip().split())))
M = int(input())
cards2 = list(map(int, input().strip().split()))
result = []
for card in cards2:
    result.append('1' if card in cards else '0')

print(' '.join(result))