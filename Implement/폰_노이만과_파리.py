import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
S, T, D = map(int, input().split())

cal1 = D//(S*2)
cal2 = cal1*T
print (cal2)