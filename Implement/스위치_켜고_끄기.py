import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
switch_n = int(input())
arr = list(map(int, input().split()))
students = int(input())
students_info = [list(map(int, input().split())) for _ in range(students)]
  
  
def maleSwitch(n):
  for i in range(n - 1, switch_n, n):
    arr[i] ^= 1
    
def femaleSwitch(n):
  n -= 1
  arr[n] ^= 1
  left, right = n - 1, n + 1
  while left >= 0 and right < switch_n and arr[left] == arr[right]:
    arr[left] ^= 1
    arr[right] ^= 1
    left -= 1
    right += 1
  
for gender, n in students_info:
  if (gender == 1): # 남학생일 경우
    maleSwitch(n)
  else: # 여학생일 경우
    femaleSwitch(n)

for i in range(0, switch_n, 20):
  print (*arr[i:i+20])