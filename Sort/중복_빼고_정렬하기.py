import sys
#sys.stdin = open('./input.txt', 'r')
n = int(input())
arr = list(set(map(int, input().split())))
arr.sort()
print (*arr)