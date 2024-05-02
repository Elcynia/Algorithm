import sys
#sys.stdin = open('./input.txt', 'r')

n = int(sys.stdin.readline())
arr = [0]*10001  # 1만까지 숫자 저장

for _ in range(n):
    num = int(sys.stdin.readline())
    arr[num] += 1 # 해당 숫자의 idx에 1 +

for i in range(10001):  # 1만까지 숫자를 확인하며
    if arr[i] != 0:  # 해당 숫자가 0이 아니면
        for _ in range(arr[i]):  # 해당 숫자의 개수만큼 출력
            print(i) 