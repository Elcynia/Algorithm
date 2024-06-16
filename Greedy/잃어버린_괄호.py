import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
arr = list(input().split('-'))

# 첫 번째 부분의 합을 초기값으로 설정
ans = sum(map(int, arr[0].split('+')))

# 나머지 부분의 합 제거
for part in arr[1:]:
    ans -= sum(map(int, part.split('+')))
print (ans)