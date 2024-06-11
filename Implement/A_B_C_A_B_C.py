import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())

res1 = a + b - c
res2 = int(str(a) + str(b)) - c
print (res1, res2, sep='\n')