import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
  a, b, c = map(int, input().split())
  triangle =  sorted([a, b, c])

  if (triangle[0]**2 + triangle[1]**2 == triangle[2]**2):
    print(f"Scenario #{i}:\nyes\n")
  else:
    print(f"Scenario #{i}:\nno\n")
    