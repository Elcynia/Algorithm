# import sys
# sys.stdin = open('input.txt', 'rt')
n = int(input())
for i in range(1,n+1):
  spaces = ' ' * (n-i)
  stars = '*'*i
  print (f'{spaces}{stars}')