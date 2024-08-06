import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
triangle = []
ans = ''
for _ in range(n):
  triangle.append(int(input()))
  
triangle.sort(reverse=True)
for i in range(n-2):
  if (triangle[i] < triangle[i+1] + triangle[i+2]):
    ans = triangle[i] + triangle[i+1] + triangle[i+2]
    break
  else:
    ans = -1
print (ans)