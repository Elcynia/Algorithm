import sys, math
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

for i in nums:
    sqrt = int(math.sqrt(i))
    if sqrt * sqrt == i:
        print(1, end=' ')
    else:
        print(0, end=' ')