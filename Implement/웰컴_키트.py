import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))
t, p = map(int, input().split())
total = sum(arr)
ans = 0

for i in arr:
    # 필요한 만큼 나누기
    if i % t == 0:
        ans += i // t
    else:
        ans += (i // t) + 1


p_ans1 = total // p
p_ans2 = total % p

print(ans)
print(p_ans1, p_ans2)
