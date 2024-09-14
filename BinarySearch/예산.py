import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
limit_budget = int(input())
left, right = 0, arr[-1]
mx_budget = 0

def calculate_budget(arr, limit):
    return sum(min(x, limit) for x in arr)
  
while left <= right:
  mid = (left + right) // 2
  if calculate_budget(arr, mid) <= limit_budget:
    mx_budget = mid
    left = mid + 1
  else:
    right = mid - 1
print (mx_budget)