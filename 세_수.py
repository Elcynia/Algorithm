import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
arr = sorted(list(map(int, input().split())))
print(arr[1])
