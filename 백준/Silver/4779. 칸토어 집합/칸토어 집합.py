import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

def recur(x):
  if x == 0:
    return '-'
  prev = recur(x-1)
  return prev + " " * (3**(x-1)) + prev

while True:
  try:
    n = int(input().strip())
    print(recur(n))
  except ValueError:
    break