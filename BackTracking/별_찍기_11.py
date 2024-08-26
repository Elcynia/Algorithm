import sys
sys.stdin = open('./input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
default_height = 3
stars = ["  *  ", " * * ", "*****"]

def func(n):
  if n == 3:
    return ['  *  ', ' * * ', '*****']
  
  stars = func(n // 2)
  new = []
  for star in stars:
    new.append(' ' * (n // 2) + star + ' ' * (n // 2))
  for star in stars:
    new.append(star + ' ' + star)
  return new

for i in func(n):
  print (i)