import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().strip().split())
dic1 = {input().strip(): i for i in range(1, N + 1)}
dic2 = {num: name for name, num in dic1.items()}

for _ in range(M):
    pocketmon = input().strip()
    if pocketmon.isdigit():
        print(dic2[int(pocketmon)])
    else:
        print(dic1[pocketmon])