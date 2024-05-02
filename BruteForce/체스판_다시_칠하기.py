import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
ans = []

arr = [input().strip() for _ in range(n)]

for i in range(n - 7):
    for j in range(m - 7): # 8x8 체스판을 만들 수 있는 모든 경우의 수를 탐색
        cnt1 = 0 
        cnt2 = 0 
        for x in range(i, i + 8): # 8x8 체스판을 만들어서
            for y in range(j, j + 8): # W로 시작하는 경우와 B로 시작하는 경우를 나눠서
                if (x + y) % 2 == 0:  # 짝수번째 칸은 W로 시작
                    if arr[x][y] != 'W': cnt1 += 1 # W로 시작하는 경우에 B로 칠해져 있는 칸의 개수
                    if arr[x][y] != 'B': cnt2 += 1 # B로 시작하는 경우에 W로 칠해져 있는 칸의 개수
                else : # 홀수번째 칸은 B로 시작
                    if arr[x][y] != 'W': cnt2 += 1 
                    if arr[x][y] != 'B': cnt1 += 1 
        ans.append(cnt1)
        ans.append(cnt2)

print(min(ans))