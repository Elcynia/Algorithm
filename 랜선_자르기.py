import sys
sys.stdin = open('./input.txt', 'r')
K, N = map(int, sys.stdin.readline().split())
line = []
res = 0
largest =  0

def Count(len):
  cnt = 0
  for x in line:
    cnt += (x//len)
  return cnt

for i in range(K):
  tmp = int(sys.stdin.readline())
  line.append(tmp)
  largest = max(largest, tmp)
left = 1
right = largest

while left <= right:
  mid = (left+right) // 2
  if Count(mid) >= N:
    res = mid
    left = mid + 1 
  else:
    right = mid - 1
    
print (res)