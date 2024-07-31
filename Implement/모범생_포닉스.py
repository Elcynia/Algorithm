import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
t = list(map(int, input().split()))
cal1 = (len(t)-1)*8 + sum(t)
print (cal1 // 24, cal1 % 24)