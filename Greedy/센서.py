import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input()) # 센서 수
k = int(input()) # 집중국 수
arr = list(map(int, input().strip().split())) # n개의 센서 좌표들
ans = []
if n <= k:
  print (0)
else:
  arr.sort()
  for i in range(1, n): 
    ans.append(arr[i] - arr[i-1])
    
  ans.sort(reverse=True)
  for _ in range(k-1):
      ans.pop(0)

  print (sum(ans))