import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
arr = list(input().strip())
print (''.join(arr[-5:]))