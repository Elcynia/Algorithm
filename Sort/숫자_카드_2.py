import sys
from collections import Counter
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N = int(input())
cards = sorted(list(map(int, input().split()))) # 카드
M = int(input())
nums = list(map(int, input().split())) # 찾을 숫자

cnt = Counter(cards)
 
for num in nums:
    if num in cnt:
        print(cnt[num], end=' ')
    else:
        print(0, end=' ')