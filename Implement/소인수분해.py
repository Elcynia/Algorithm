import sys
#sys.stdin = open('./input.txt', 'r')
n = int(input())
a = 2

while a * a <= n:
    if n % a == 0:
        print(a)
        n = n // a
    else:
        a += 1
if n > 1:
    print(n)
