import sys
sys.stdin = open("input.txt", "r")
chess = list(map(int, input().split(' ')))
a =[1,1,2,2,2,8]
for i in range(6):
    print(a[i]-chess[i], end=' ')