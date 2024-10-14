import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
cnt = 0
chongchong = {'ChongChong'}

for _ in range(n):
  a, b = input().strip().split()
  if a in chongchong or b in chongchong:
    chongchong.add(a)
    chongchong.add(b)

print(len(chongchong))