import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())

def fibonacci(digit):
  if (digit <= 1):
    return digit
  return fibonacci(digit-1) + fibonacci(digit-2)
  
  
print(fibonacci(n))