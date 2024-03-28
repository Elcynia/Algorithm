import sys
sys.stdin = open('./input.txt', 'rt')
def gcd(a,b):
  if (b == 0):
    return a
  return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)
a,b = map(int, input().split())
print(gcd(a,b),lcm(a,b), end='\n')