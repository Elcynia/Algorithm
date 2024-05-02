import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

n = int(input())
f = int(input())
ans = (n // 100) * 100

for i in range(f):
    if (ans + i) % f == 0:
        ans += i
        break
print (str(ans)[-2:])