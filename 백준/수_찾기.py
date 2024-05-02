import sys
sys.stdin = open('./input.txt', 'r')
N = int(sys.stdin.readline())
N_arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_arr = list(map(int, sys.stdin.readline().split()))
N_arr.sort()

def bs(arr, target):
  left, right = 0, len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return True 
    elif arr[mid] < target:
        left = mid + 1 
    else: 
       right = mid - 1
  return False


for i in M_arr:
    if bs(N_arr, i):
        print(1)
    else:
        print(0)