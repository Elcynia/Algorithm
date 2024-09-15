import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N = int(input())
building = [int(input()) for _ in range(N)]
S = []
cnt = 0

for i in range(N):
    while S and S[-1] <= building[i]:
        S.pop()
    
    S.append(building[i])
    cnt += len(S) -1
print (cnt)