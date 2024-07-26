import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

h,i,a,r,c = map(int, input().split())

cal1 = h*i
cal2 = a*r*c
print (cal1 - cal2)