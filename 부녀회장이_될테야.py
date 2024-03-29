import sys
sys.stdin = open('./input.txt', 'r')
t = int(sys.stdin.readline())
for _ in range(t):
  k = int(sys.stdin.readline()) # 층 수
  n = int(sys.stdin.readline()) # 호 수
  for i in range(1, n+1): 
    arr = [j for j in range(1, i+1)]
    for _ in range(1, k+1):
      for el in range(1, i):
        arr[el] += arr[el-1]
  print(arr[-1])