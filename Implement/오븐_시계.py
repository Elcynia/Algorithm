import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
h, m = map(int, input().split())
runtime = int(input())

m += runtime
if m >= 60:
    h += m // 60
    m %= 60
if h >= 24:
    h %= 24
print(h, m)