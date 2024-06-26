import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.read
n, arr = list(map(int, input().split()))
n = arr[0]
arr.remove(arr[0])
ans = []
for i in arr:
  ans.append(int(str(i)[::-1].lstrip('0')))

ans.sort()
for i in ans:
  print (i)
  
'''
N, *S = input().split()
for i in range(int(N)):
    S[i] = S[i][::-1]
S = list(map(int, S))
print(*sorted(S), sep="\n")
'''  