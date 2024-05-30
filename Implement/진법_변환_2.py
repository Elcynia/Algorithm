import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, B = map(int, input().split())

def convert(N, B):
    if N == 0:
        return 0
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while N > 0:
        res = digits[N % B] + res
        N = N // B
    return res

print(convert(N,B))