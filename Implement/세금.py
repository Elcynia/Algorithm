import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
cal1 = int((22 / 100) * n)
tmp =  int((20 / 100) * n)
cal2 = int((22 / 100) * tmp)
print (n - cal1, n - cal2)