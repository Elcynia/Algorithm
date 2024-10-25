import sys
from collections import Counter
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
# uospc
n = int(input())
s = list(input().strip())
s_cnt = Counter(s)
uospc_count = [s_cnt['u'], s_cnt['o'], s_cnt['s'], s_cnt['p'], s_cnt['c']]
r = min(uospc_count)
print(r)