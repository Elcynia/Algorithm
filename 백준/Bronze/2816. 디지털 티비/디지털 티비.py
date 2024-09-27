import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
kbs1_idx, kbs2_idx = 0, 0

for i in range(n):
    chnl = input().strip()
    if chnl == "KBS1":
        kbs1_idx = i
    if chnl == "KBS2":
        kbs2_idx = i

if kbs1_idx > kbs2_idx:
    kbs2_idx += 1

result = '1' * kbs1_idx + '4' * kbs1_idx

if kbs2_idx != 1:
    result += '1' * kbs2_idx + '4' * (kbs2_idx - 1)

print(result)