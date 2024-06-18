import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
weights = [int(input()) for _ in range(n)]
weights.sort(reverse=True)
max_weight = 0

for i in range(n):
    current_weight = weights[i] * (i + 1)
    if current_weight > max_weight:
        max_weight = current_weight

print(max_weight)