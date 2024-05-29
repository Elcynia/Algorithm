import sys
sys.stdin = open('./input.txt', 'r')

a = int(input())
b = int(input())

c1 = a * (b % 10)
c2 = a * ((b // 10) % 10)
c3 = a * (b // 100)

print(c1)
print(c2)
print(c3)
print(a*b)