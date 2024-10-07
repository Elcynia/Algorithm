import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
arr = input().strip()
a_cnt = arr.count('a')
arr = arr * 2 # 원형 문자열 처리를 위해 2번 반복
min_swaps = float('inf')

for i in range(len(arr) // 2):
    window = arr[i:i + a_cnt]
    b_cnt = window.count('b')
    min_swaps = min(min_swaps, b_cnt)

print(min_swaps)