import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
for i in range(n):
    result += sum(arr[:i+1])
    print (result)
print(result)
