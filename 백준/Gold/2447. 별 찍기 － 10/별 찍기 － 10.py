import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())

def recur(n):
  if n == 1:
    return ['*']
  
  stars = recur(n // 3)
  result = []
  
  for s in stars:
    result.append(s * 3)  # 첫 번째 줄
  for s in stars:
    result.append(s + ' ' * (n // 3) + s)  # 중간 줄 (빈칸 포함)
  for s in stars:
    result.append(s * 3)  # 마지막 줄
  
  return result

print(*recur(n), sep='\n')