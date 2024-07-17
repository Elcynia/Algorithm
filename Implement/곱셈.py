import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
a, b, c = map(int, input().split())
print(pow(a, b, c))