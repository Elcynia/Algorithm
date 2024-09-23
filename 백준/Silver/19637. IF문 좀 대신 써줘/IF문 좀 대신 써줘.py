import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())

titles = []
powers = []

for _ in range(N):
  title, power = input().split()
  titles.append(title)
  powers.append(int(power))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left
for _ in range(M):
  status = int(input())
  index = binary_search(powers, status)
  print(titles[index])
