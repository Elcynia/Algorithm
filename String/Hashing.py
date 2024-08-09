import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
L = int(input()) # 문자열 길이
s = list(input().strip())
ans = 0

for i in range(L):
    char = ord(s[i]) - ord('a') + 1
    ans += char * (31 ** i)
    ans %= 1234567891

print(ans)